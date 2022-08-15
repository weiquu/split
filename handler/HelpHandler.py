def help(update, context):
    msg = 'Welcome to $plit! Please find a list of commands below' + '\n'
    msg += '/creategroup - Creates a new group of expenses to split' + '\n'
    msg += '/entergroup - Enters a group for you to split expenses' + '\n'
    msg += '/addusers - Adds users to the group you are currently in' + '\n' 
    msg += '/viewusers - Views the users in the group you are currently in' + '\n'
    msg += '/expense - Adds an expense to the group you are currently in' + '\n'
    msg += '/viewall - Views all expenses in the group you are currently in, including those which have been split' + '\n'
    msg += '/outstanding - Views the expenses which have not been split in the group you are currently in' + '\n'
    msg += '/split - Shows you the split (i.e. who pays who how much). To finalise the split and mark the expenses as split, press yes; else, press no' + '\n'
    update.message.reply_text(msg)