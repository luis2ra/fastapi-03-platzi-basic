# type_error: al ingresar un Path parametro errado para "id"
# http://0.0.0.0:8080/movies/dos
{
	"detail": [
		{
			"loc": [
				"path",
				"id"
			],
			"msg": "value is not a valid integer",
			"type": "type_error.integer"
		}
	]
}

# value_error: probando Path con la validacion ge=1 para "id"
# http://0.0.0.0:8080/movies/0
{
	"detail": [
		{
			"loc": [
				"path",
				"id"
			],
			"msg": "ensure this value is greater than or equal to 1",
			"type": "value_error.number.not_ge",
			"ctx": {
				"limit_value": 1
			}
		}
  	]
}

# value_error: probando Path con la validacion le=2000 para "id"
# http://0.0.0.0:8080/movies/2002
{
	"detail": [
		{
			"loc": [
				"path",
				"id"
			],
			"msg": "ensure this value is less than or equal to 2000",
			"type": "value_error.number.not_le",
			"ctx": {
				"limit_value": 2000
			}
		}
	]
}

# value_error: probando Query con la validacion min_length=5 para "category"
# http://0.0.0.0:8080/movies/?category=Acc&year=2022
{
	"detail": [
		{
			"loc": [
				"body",
				"title"
			],
			"msg": "ensure this value has at least 5 characters",
			"type": "value_error.any_str.min_length",
			"ctx": {
				"limit_value": 5
			}
		}
	]
}

# value_error: probando Query con la validacion le=2023 para "year"
# http://0.0.0.0:8080/movies/?category=Accion&year=2025
{
	"detail": [
		{
			"loc": [
				"query",
				"year"
			],
			"msg": "ensure this value is less than or equal to 2023",
			"type": "value_error.number.not_le",
			"ctx": {
				"limit_value": 2023
			}
		}
	]
}


# value_error
{
	"detail": [
		{
			"loc": [
				"query",
				"year"
			],
			"msg": "ensure this value is less than or equal to 2023",
			"type": "value_error.number.not_le",
			"ctx": {
				"limit_value": 2023
			}
		}
	]
}

# value_error
{
	"detail": [
		{
			"loc": [
				"body",
				"year"
			],
			"msg": "ensure this value is less than or equal to 2023",
			"type": "value_error.number.not_le",
			"ctx": {
				"limit_value": 2023
			}
		}
	]
}

