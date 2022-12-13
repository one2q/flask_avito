from hashlib import md5

a = 'https://www.gravatar.com/avatar/' + md5(b'val8673@gmail.com').hexdigest()


q = ['ssd', 'srtrht', 'sd', 'sderw']

def wer(li):

	min_word = min(q, key=len)

	for i in range(len(min_word)):
		for word in q:
			if word[i] != min_word[i]:
				return min_word[:i]
	return min_word


print(wer(q))