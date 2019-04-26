import math

from django import template

register = template.Library()


@register.filter
def ci(business):
    total = business.total_reviews
    positive = business.positive_reviews
    z = 1.96
    phat = 1.0 * positive / total
    score = (phat + z * z / (2 * total) - z * math.sqrt((phat * (1 - phat) + z * z / (4 * total)) / total)) / (
            1 + z * z / total)

    score = round(score * 5, 1)
    return score


@register.filter
def round_ratings(business):
    return round(business.ratings * 5, 1)
