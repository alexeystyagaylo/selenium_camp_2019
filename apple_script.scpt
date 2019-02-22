tell application "System Events"
	if exists (processes where name is "SecurityAgent") then
		tell process "SecurityAgent" to keystroke "*****"
		delay 0.5
		tell application "System Events" to keystroke return
		delay 0.5
	end if
end tell
