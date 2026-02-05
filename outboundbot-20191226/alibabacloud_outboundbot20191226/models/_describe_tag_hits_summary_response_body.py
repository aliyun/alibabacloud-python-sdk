# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class DescribeTagHitsSummaryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        tag_groups: List[main_models.DescribeTagHitsSummaryResponseBodyTagGroups] = None,
        tag_hits_list: List[main_models.DescribeTagHitsSummaryResponseBodyTagHitsList] = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.tag_groups = tag_groups
        self.tag_hits_list = tag_hits_list

    def validate(self):
        if self.tag_groups:
            for v1 in self.tag_groups:
                 if v1:
                    v1.validate()
        if self.tag_hits_list:
            for v1 in self.tag_hits_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['TagGroups'] = []
        if self.tag_groups is not None:
            for k1 in self.tag_groups:
                result['TagGroups'].append(k1.to_map() if k1 else None)

        result['TagHitsList'] = []
        if self.tag_hits_list is not None:
            for k1 in self.tag_hits_list:
                result['TagHitsList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.tag_groups = []
        if m.get('TagGroups') is not None:
            for k1 in m.get('TagGroups'):
                temp_model = main_models.DescribeTagHitsSummaryResponseBodyTagGroups()
                self.tag_groups.append(temp_model.from_map(k1))

        self.tag_hits_list = []
        if m.get('TagHitsList') is not None:
            for k1 in m.get('TagHitsList'):
                temp_model = main_models.DescribeTagHitsSummaryResponseBodyTagHitsList()
                self.tag_hits_list.append(temp_model.from_map(k1))

        return self

class DescribeTagHitsSummaryResponseBodyTagHitsList(DaraModel):
    def __init__(
        self,
        hit_count: int = None,
        tag_group: str = None,
        tag_name: str = None,
    ):
        self.hit_count = hit_count
        self.tag_group = tag_group
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hit_count is not None:
            result['HitCount'] = self.hit_count

        if self.tag_group is not None:
            result['TagGroup'] = self.tag_group

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HitCount') is not None:
            self.hit_count = m.get('HitCount')

        if m.get('TagGroup') is not None:
            self.tag_group = m.get('TagGroup')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

class DescribeTagHitsSummaryResponseBodyTagGroups(DaraModel):
    def __init__(
        self,
        id: str = None,
        script_id: str = None,
        tag_group: str = None,
        tag_group_index: int = None,
    ):
        # ID
        self.id = id
        self.script_id = script_id
        self.tag_group = tag_group
        self.tag_group_index = tag_group_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.tag_group is not None:
            result['TagGroup'] = self.tag_group

        if self.tag_group_index is not None:
            result['TagGroupIndex'] = self.tag_group_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('TagGroup') is not None:
            self.tag_group = m.get('TagGroup')

        if m.get('TagGroupIndex') is not None:
            self.tag_group_index = m.get('TagGroupIndex')

        return self

