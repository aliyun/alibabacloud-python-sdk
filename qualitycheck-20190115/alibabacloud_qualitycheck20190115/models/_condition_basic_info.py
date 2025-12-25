# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class ConditionBasicInfo(DaraModel):
    def __init__(
        self,
        check_range: main_models.ConditionBasicInfoCheckRange = None,
        cid: str = None,
        exclusion: int = None,
        id: int = None,
        lambda_: str = None,
        name: str = None,
        operators: List[main_models.OperatorBasicInfo] = None,
        rid: str = None,
        user_group: str = None,
    ):
        self.check_range = check_range
        self.cid = cid
        self.exclusion = exclusion
        self.id = id
        self.lambda_ = lambda_
        self.name = name
        self.operators = operators
        self.rid = rid
        self.user_group = user_group

    def validate(self):
        if self.check_range:
            self.check_range.validate()
        if self.operators:
            for v1 in self.operators:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_range is not None:
            result['Check_range'] = self.check_range.to_map()

        if self.cid is not None:
            result['Cid'] = self.cid

        if self.exclusion is not None:
            result['Exclusion'] = self.exclusion

        if self.id is not None:
            result['Id'] = self.id

        if self.lambda_ is not None:
            result['Lambda'] = self.lambda_

        if self.name is not None:
            result['Name'] = self.name

        result['Operators'] = []
        if self.operators is not None:
            for k1 in self.operators:
                result['Operators'].append(k1.to_map() if k1 else None)

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.user_group is not None:
            result['UserGroup'] = self.user_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Check_range') is not None:
            temp_model = main_models.ConditionBasicInfoCheckRange()
            self.check_range = temp_model.from_map(m.get('Check_range'))

        if m.get('Cid') is not None:
            self.cid = m.get('Cid')

        if m.get('Exclusion') is not None:
            self.exclusion = m.get('Exclusion')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Lambda') is not None:
            self.lambda_ = m.get('Lambda')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.operators = []
        if m.get('Operators') is not None:
            for k1 in m.get('Operators'):
                temp_model = main_models.OperatorBasicInfo()
                self.operators.append(temp_model.from_map(k1))

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('UserGroup') is not None:
            self.user_group = m.get('UserGroup')

        return self

class ConditionBasicInfoCheckRange(DaraModel):
    def __init__(
        self,
        absolute: bool = None,
        all_sentences_satisfy: bool = None,
        anchor: main_models.ConditionBasicInfoCheckRangeAnchor = None,
        range: main_models.ConditionBasicInfoCheckRangeRange = None,
        role: str = None,
        role_id: int = None,
    ):
        self.absolute = absolute
        self.all_sentences_satisfy = all_sentences_satisfy
        self.anchor = anchor
        self.range = range
        self.role = role
        self.role_id = role_id

    def validate(self):
        if self.anchor:
            self.anchor.validate()
        if self.range:
            self.range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.absolute is not None:
            result['Absolute'] = self.absolute

        if self.all_sentences_satisfy is not None:
            result['AllSentencesSatisfy'] = self.all_sentences_satisfy

        if self.anchor is not None:
            result['Anchor'] = self.anchor.to_map()

        if self.range is not None:
            result['Range'] = self.range.to_map()

        if self.role is not None:
            result['Role'] = self.role

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Absolute') is not None:
            self.absolute = m.get('Absolute')

        if m.get('AllSentencesSatisfy') is not None:
            self.all_sentences_satisfy = m.get('AllSentencesSatisfy')

        if m.get('Anchor') is not None:
            temp_model = main_models.ConditionBasicInfoCheckRangeAnchor()
            self.anchor = temp_model.from_map(m.get('Anchor'))

        if m.get('Range') is not None:
            temp_model = main_models.ConditionBasicInfoCheckRangeRange()
            self.range = temp_model.from_map(m.get('Range'))

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        return self

class ConditionBasicInfoCheckRangeRange(DaraModel):
    def __init__(
        self,
        from_: int = None,
        to: int = None,
    ):
        self.from_ = from_
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self



class ConditionBasicInfoCheckRangeAnchor(DaraModel):
    def __init__(
        self,
        cid: str = None,
        hit_time: int = None,
        location: str = None,
    ):
        self.cid = cid
        self.hit_time = hit_time
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cid is not None:
            result['Cid'] = self.cid

        if self.hit_time is not None:
            result['Hit_time'] = self.hit_time

        if self.location is not None:
            result['Location'] = self.location

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')

        if m.get('Hit_time') is not None:
            self.hit_time = m.get('Hit_time')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        return self

