extends Control


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	var lines1 = []
	var lines2 = []
	for i in range(50):
		lines1.append(str(randfn(0, 1))) # random values with mean = 0, std = 1
		lines2.append(str(randfn(10, 1))) # random values with mean = 10, std = 1
	$Panel/HBoxContainer/TextEdit.text = '\n'.join(lines1)
	$Panel/HBoxContainer/TextEdit2.text = '\n'.join(lines2)
	$Panel/HBoxContainer2/LineEdit.text = str(randf() * 10) 
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass


func _on_button_button_down() -> void:
	var x1 = []
	for x in  $Panel/HBoxContainer/TextEdit.text.split('\n'):
		x1.append(float(x))
	
	var x2 = []
	for x in  $Panel/HBoxContainer/TextEdit2.text.split('\n'):
		x2.append(float(x))
	
	var json = JSON.stringify({'x1': x1, 'x2': x2, 'input': float($Panel/HBoxContainer2/LineEdit.text)})
	var cmd = "run_py(`run('%s')`);" % json
	var js_return = JavaScriptBridge.eval(cmd)
	print (['sent ', cmd])
	print(['got ', js_return]) # prints '3.0'
	$Panel/HBoxContainer2/LineEdit.text = 'Result: %s' % js_return
