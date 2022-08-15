def help():
    str = 'Welcome to $plit! Please find a list of commands below' + '\n'
    str += '/creategroup - Creates a new group of expenses to split' + '\n'
    str += '/entergroup - Enters a group for you to split expenses' + '\n'
    str += '/addusers - Adds users to the group you are currently in' + '\n' 
    str += '/viewusers - Views the users in the group you are currently in' + '\n'
    str += '/expense - Adds an expense to the group you are currently in' + '\n'
    str += '/viewall - Views all expenses in the group you are currently in, including those which have been split' + '\n'
    str += '/outstanding - Views the expenses which have not been split in the group you are currently in' + '\n'
    str += '/split - Shows you the split (i.e. who pays who how much). To finalise the split and mark the expenses as split, press yes; else, press no' + '\n'
    return str