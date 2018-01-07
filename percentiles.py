# percentile scoring
# based on think stats with python

def percentileRank(scores, your_score):
	count = 0
	for score in scores:
		if your_score >= score:
			count += 1
	
	rank = 100.0 * (count / len(scores))
	return rank
	
def percentile(scores, percentile_rank):
	scores.sort()
	for score in scores:
		if percentileRank(score, scores) >= percentile_rank:
			return score