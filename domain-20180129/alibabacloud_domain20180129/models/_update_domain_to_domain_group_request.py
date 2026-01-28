# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateDomainToDomainGroupRequest(DaraModel):
    def __init__(
        self,
        data_source: int = None,
        domain_group_id: int = None,
        domain_name: List[str] = None,
        file_to_upload: str = None,
        lang: str = None,
        replace: bool = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.data_source = data_source
        # This parameter is required.
        self.domain_group_id = domain_group_id
        self.domain_name = domain_name
        self.file_to_upload = file_to_upload
        self.lang = lang
        # This parameter is required.
        self.replace = replace
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source is not None:
            result['DataSource'] = self.data_source

        if self.domain_group_id is not None:
            result['DomainGroupId'] = self.domain_group_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.file_to_upload is not None:
            result['FileToUpload'] = self.file_to_upload

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.replace is not None:
            result['Replace'] = self.replace

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')

        if m.get('DomainGroupId') is not None:
            self.domain_group_id = m.get('DomainGroupId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('FileToUpload') is not None:
            self.file_to_upload = m.get('FileToUpload')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Replace') is not None:
            self.replace = m.get('Replace')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

