# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetSessionListRequest(DaraModel):
    def __init__(
        self,
        action_list: List[str] = None,
        begin_date: str = None,
        client_ip_list: List[str] = None,
        client_program_list: List[str] = None,
        db_host_list: List[str] = None,
        db_id: int = None,
        db_user_list: List[str] = None,
        end_date: str = None,
        instance_id: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        session_id: str = None,
    ):
        self.action_list = action_list
        # This parameter is required.
        self.begin_date = begin_date
        self.client_ip_list = client_ip_list
        self.client_program_list = client_program_list
        self.db_host_list = db_host_list
        self.db_id = db_id
        self.db_user_list = db_user_list
        # This parameter is required.
        self.end_date = end_date
        # This parameter is required.
        self.instance_id = instance_id
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_list is not None:
            result['ActionList'] = self.action_list

        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date

        if self.client_ip_list is not None:
            result['ClientIpList'] = self.client_ip_list

        if self.client_program_list is not None:
            result['ClientProgramList'] = self.client_program_list

        if self.db_host_list is not None:
            result['DbHostList'] = self.db_host_list

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_user_list is not None:
            result['DbUserList'] = self.db_user_list

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionList') is not None:
            self.action_list = m.get('ActionList')

        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')

        if m.get('ClientIpList') is not None:
            self.client_ip_list = m.get('ClientIpList')

        if m.get('ClientProgramList') is not None:
            self.client_program_list = m.get('ClientProgramList')

        if m.get('DbHostList') is not None:
            self.db_host_list = m.get('DbHostList')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbUserList') is not None:
            self.db_user_list = m.get('DbUserList')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

