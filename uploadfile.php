<?php
foreach($_FILES as $file) {
	move_uploaded_file($file["tmp_name"], $file["name"]);
	echo "${file['name']} ${file['size']} bytes";
}
