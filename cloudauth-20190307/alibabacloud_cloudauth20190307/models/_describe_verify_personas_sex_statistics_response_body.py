# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeVerifyPersonasSexStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeVerifyPersonasSexStatisticsResponseBodyResultObject = None,
    ):
        # ID of this request.
        self.request_id = request_id
        # Returned data.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.DescribeVerifyPersonasSexStatisticsResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class DescribeVerifyPersonasSexStatisticsResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        age_0to_14cnt: int = None,
        age_0to_14rate: str = None,
        age_14to_18cnt: int = None,
        age_14to_18rate: str = None,
        age_18to_35cnt: int = None,
        age_18to_35rate: str = None,
        age_35to_50cnt: int = None,
        age_35to_50rate: str = None,
        age_50to_999cnt: int = None,
        age_50to_999rate: str = None,
        all_user_cnt: int = None,
        female_cnt: int = None,
        female_rate: str = None,
        male_cnt: int = None,
        male_rate: str = None,
    ):
        # Number of users under 14 years old.
        self.age_0to_14cnt = age_0to_14cnt
        # Proportion of users under 14 years old.
        self.age_0to_14rate = age_0to_14rate
        # Number of users between 14 and 18 years old.
        self.age_14to_18cnt = age_14to_18cnt
        # Proportion of users between 14 and 18 years old.
        self.age_14to_18rate = age_14to_18rate
        # Number of authenticated users between 18 and 35 years old.
        self.age_18to_35cnt = age_18to_35cnt
        # Proportion of authenticated users between 18 and 35 years old.
        self.age_18to_35rate = age_18to_35rate
        # Number of authenticated users between 35 and 50 years old.
        self.age_35to_50cnt = age_35to_50cnt
        # Proportion of users between 35 and 50 years old.
        self.age_35to_50rate = age_35to_50rate
        # Number of authenticated users over 50 years old.
        self.age_50to_999cnt = age_50to_999cnt
        # Proportion of authenticated users over 50 years old.
        self.age_50to_999rate = age_50to_999rate
        # Total number of authenticated users.
        self.all_user_cnt = all_user_cnt
        # Number of female users.
        self.female_cnt = female_cnt
        # Proportion of female authenticated users.
        self.female_rate = female_rate
        # Number of male users.
        self.male_cnt = male_cnt
        # Proportion of male users.
        self.male_rate = male_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.age_0to_14cnt is not None:
            result['Age0To14Cnt'] = self.age_0to_14cnt

        if self.age_0to_14rate is not None:
            result['Age0To14Rate'] = self.age_0to_14rate

        if self.age_14to_18cnt is not None:
            result['Age14To18Cnt'] = self.age_14to_18cnt

        if self.age_14to_18rate is not None:
            result['Age14To18Rate'] = self.age_14to_18rate

        if self.age_18to_35cnt is not None:
            result['Age18To35Cnt'] = self.age_18to_35cnt

        if self.age_18to_35rate is not None:
            result['Age18To35Rate'] = self.age_18to_35rate

        if self.age_35to_50cnt is not None:
            result['Age35To50Cnt'] = self.age_35to_50cnt

        if self.age_35to_50rate is not None:
            result['Age35To50Rate'] = self.age_35to_50rate

        if self.age_50to_999cnt is not None:
            result['Age50To999Cnt'] = self.age_50to_999cnt

        if self.age_50to_999rate is not None:
            result['Age50To999Rate'] = self.age_50to_999rate

        if self.all_user_cnt is not None:
            result['AllUserCnt'] = self.all_user_cnt

        if self.female_cnt is not None:
            result['FemaleCnt'] = self.female_cnt

        if self.female_rate is not None:
            result['FemaleRate'] = self.female_rate

        if self.male_cnt is not None:
            result['MaleCnt'] = self.male_cnt

        if self.male_rate is not None:
            result['MaleRate'] = self.male_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Age0To14Cnt') is not None:
            self.age_0to_14cnt = m.get('Age0To14Cnt')

        if m.get('Age0To14Rate') is not None:
            self.age_0to_14rate = m.get('Age0To14Rate')

        if m.get('Age14To18Cnt') is not None:
            self.age_14to_18cnt = m.get('Age14To18Cnt')

        if m.get('Age14To18Rate') is not None:
            self.age_14to_18rate = m.get('Age14To18Rate')

        if m.get('Age18To35Cnt') is not None:
            self.age_18to_35cnt = m.get('Age18To35Cnt')

        if m.get('Age18To35Rate') is not None:
            self.age_18to_35rate = m.get('Age18To35Rate')

        if m.get('Age35To50Cnt') is not None:
            self.age_35to_50cnt = m.get('Age35To50Cnt')

        if m.get('Age35To50Rate') is not None:
            self.age_35to_50rate = m.get('Age35To50Rate')

        if m.get('Age50To999Cnt') is not None:
            self.age_50to_999cnt = m.get('Age50To999Cnt')

        if m.get('Age50To999Rate') is not None:
            self.age_50to_999rate = m.get('Age50To999Rate')

        if m.get('AllUserCnt') is not None:
            self.all_user_cnt = m.get('AllUserCnt')

        if m.get('FemaleCnt') is not None:
            self.female_cnt = m.get('FemaleCnt')

        if m.get('FemaleRate') is not None:
            self.female_rate = m.get('FemaleRate')

        if m.get('MaleCnt') is not None:
            self.male_cnt = m.get('MaleCnt')

        if m.get('MaleRate') is not None:
            self.male_rate = m.get('MaleRate')

        return self

