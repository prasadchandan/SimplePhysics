import dearpygui.dearpygui as dpg 
import geometry as g

def redraw(k:g.Kernel, w:g.WorldConfig):
  dpg.delete_item("canvas", children_only=True, )
  # for p in k.points.values():
  #   dpg.draw_circle(p.position, 6, fill=(255, 255, 255, 255), parent="canvas")
  
  for l in k.lines.values():
    p1 = g.get_point(k, l.pt_1_id)
    p2 = g.get_point(k, l.pt_2_id)
    dpg.draw_line(p1.position, p2.position, color=(255, 0, 0, 255), thickness=1, parent="canvas")

  for p in k.points.values():
    dpg.draw_circle(p.position, 6, fill=(255, 255, 255, 255), parent="canvas")

def draw(k:g.Kernel, w:g.WorldConfig):
  w.width = 800
  w.height = 600
  dpg.create_context()
  with dpg.window(label="Main Window", tag="MainWindow", autosize=True):
    with dpg.drawlist(width=800, height=600, tag="canvas"):
      redraw(k, w)
      ## IDEA: Create a dpg.node and use translate to move the points around rather 
      ## .     than redrawing each time?

  dpg.create_viewport(title='Simple Physics Engine', width=840, height=640)
  dpg.set_primary_window('MainWindow', True)
  dpg.setup_dearpygui()
  dpg.show_viewport()
  
  while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    #print("this will run every frame")
    g.simulate_step(k, w)
    redraw(k, w)
    dpg.render_dearpygui_frame()