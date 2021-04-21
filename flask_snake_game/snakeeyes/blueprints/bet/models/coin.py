def add_subscription_coins(coins, previous_plan, plan, cancelled_on):
	"""
	Add exixting amount of coin to an existing coin value

	:param coins: Exixting coin value 
	:param type: int
	:param previous_plan: previous subscription plan 
	:param type: dict
	:param plan: New subscription plan 
	:param type : dict
	:param cancelled_on: when a plan has potentially been canceled 
	:param type : datetime
	:return: int
	"""	

	previous_plan_coins = 0
	plan_coins = plan['metadata']['coins']

	if previous_plan:
		previous_plan_coins = previous_plan['metadata']['coins']

	if cancelled_on is None and plan_coins == previous_plan_coins:
		coin_adjustment = plan_coins
	elif plan_coins <= previous_plan_coins:
		return coins
	else:
		# addin only the difference between the upgrading plan 
		# because tey were already credited the previous plan's coins
		coin_adjustment = plan_coins - previous_plan_coins

	return coins + coin_adjustment

