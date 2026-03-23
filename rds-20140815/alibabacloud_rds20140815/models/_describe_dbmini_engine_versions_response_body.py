# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBMiniEngineVersionsResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        max_records_per_page: int = None,
        minor_version_items: List[main_models.DescribeDBMiniEngineVersionsResponseBodyMinorVersionItems] = None,
        page_numbers: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.max_records_per_page = max_records_per_page
        self.minor_version_items = minor_version_items
        self.page_numbers = page_numbers
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.minor_version_items:
            for v1 in self.minor_version_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.max_records_per_page is not None:
            result['MaxRecordsPerPage'] = self.max_records_per_page

        result['MinorVersionItems'] = []
        if self.minor_version_items is not None:
            for k1 in self.minor_version_items:
                result['MinorVersionItems'].append(k1.to_map() if k1 else None)

        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('MaxRecordsPerPage') is not None:
            self.max_records_per_page = m.get('MaxRecordsPerPage')

        self.minor_version_items = []
        if m.get('MinorVersionItems') is not None:
            for k1 in m.get('MinorVersionItems'):
                temp_model = main_models.DescribeDBMiniEngineVersionsResponseBodyMinorVersionItems()
                self.minor_version_items.append(temp_model.from_map(k1))

        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDBMiniEngineVersionsResponseBodyMinorVersionItems(DaraModel):
    def __init__(
        self,
        community_minor_version: str = None,
        engine: str = None,
        engine_version: str = None,
        expire_date: str = None,
        expire_status: str = None,
        is_hotfix_version: bool = None,
        minor_version: str = None,
        node_type: str = None,
        release_note: str = None,
        release_type: str = None,
        status_desc: str = None,
        tag: str = None,
    ):
        self.community_minor_version = community_minor_version
        self.engine = engine
        self.engine_version = engine_version
        self.expire_date = expire_date
        self.expire_status = expire_status
        self.is_hotfix_version = is_hotfix_version
        self.minor_version = minor_version
        self.node_type = node_type
        self.release_note = release_note
        self.release_type = release_type
        self.status_desc = status_desc
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.community_minor_version is not None:
            result['CommunityMinorVersion'] = self.community_minor_version

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.expire_status is not None:
            result['ExpireStatus'] = self.expire_status

        if self.is_hotfix_version is not None:
            result['IsHotfixVersion'] = self.is_hotfix_version

        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note

        if self.release_type is not None:
            result['ReleaseType'] = self.release_type

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommunityMinorVersion') is not None:
            self.community_minor_version = m.get('CommunityMinorVersion')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('ExpireStatus') is not None:
            self.expire_status = m.get('ExpireStatus')

        if m.get('IsHotfixVersion') is not None:
            self.is_hotfix_version = m.get('IsHotfixVersion')

        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')

        if m.get('ReleaseType') is not None:
            self.release_type = m.get('ReleaseType')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

