# try/else从句

Often times we might want some code to run if no exception occurs. This can easily be achieved by using an else clause. One might ask: why, if you only want some code to run if no exception occurs, wouldn’t you simply put that code inside the try? The answer is that then any exceptions in that code will be caught by the try, and you might not want that. Most people don’t use it and honestly I have myself not used it widely. Here is an example:

try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # any code that should only run if no exception occurs in the try,
    # but for which exceptions should NOT be caught
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')

# Output: I am sure no exception is going to occur!
# This would only run if no exception occurs.
# This would be printed in every case.
The else clause would only run if no exception occurs and it would run before the finally clause.