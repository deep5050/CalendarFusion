#!/usr/bin/env python


def get_lang_dict(lang="en"):
    dic = {}
    colnames = ["Week", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    colnames_ja = ["週", "月", "火", "水", "木", "金", "土", "日"]
    colnames_tw = ["週", "一", "二", "三", "四", "五", "六", "日"]  # Taiwan
    colnames_hi = [
        "सप्ताह",
        "सोम",
        "मंगल",
        "बुध",
        "गुरु",
        "शुक्र",
        "शनि",
        "रवि",
    ]  # Hindi
    colnames_bn = [
        "সপ্তাহ",
        "সোম",
        "মঙ্গল",
        "বুধ",
        "বৃহঃ",
        "শুক্র",
        "শনি",
        "রবি",
    ]  # Bengali

    if lang == "en":
        for col in colnames:
            dic[col] = col
    elif lang == "tw":
        for col, colja in zip(colnames, colnames_tw):
            dic[col] = colja
    elif lang == "ja":
        for col, colja in zip(colnames, colnames_ja):
            dic[col] = colja
    elif lang == "hi":
        for col, colja in zip(colnames, colnames_hi):
            dic[col] = colja
    elif lang == "bn":
        for col, colja in zip(colnames, colnames_bn):
            dic[col] = colja
    else:
        for col in colnames:
            dic[col] = col
    return dic
