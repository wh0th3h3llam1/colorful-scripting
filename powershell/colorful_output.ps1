# GitHub: https://github.com/wh0th3h3llam1
# Author: wh0th3h3llam1

# A module "PSWriteColor" is required for this to work
# It can be installed using below command
# Install-Module -Name PSWriteColor -RequiredVersion 0.86

Write-Color -Text "[SUCCESS]", "Module Installed Successfully" -Color Green, White
Write-Color -Text "[INFO] ", "Files Updated Successfully" -C Cyan, White

Write-Color -Text "[WARNING]", "No Admin Permissions, All features will not be available" -Color Yellow, White
Write-Color -Text "[ERROR] ", "Couldn't update system" -C Red, White


# Allowed Colors
	# Black,
	# DarkBlue,
	# DarkGreen,
	# DarkCyan,
	# DarkRed,
	# DarkMagenta,
	# DarkYellow,
	# Gray,
	# DarkGray,
	# Blue,
	# Green,
	# Cyan,
	# Red,
	# Magenta,
	# Yellow,
	# White,
