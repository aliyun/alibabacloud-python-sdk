# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ExportOASRequest(DaraModel):
    def __init__(
        self,
        api_id_list: List[str] = None,
        data_format: str = None,
        group_id: str = None,
        oas_version: str = None,
        page_number: int = None,
        security_token: str = None,
        stage_name: str = None,
        with_xextensions: bool = None,
    ):
        # The APIs that you want to export.
        self.api_id_list = api_id_list
        # The exported format:
        # 
        # *   json
        # *   yaml
        self.data_format = data_format
        # The API group ID.
        self.group_id = group_id
        # The OAS version. Valid values:
        # 
        # *   **oas2**
        # *   **oas3**
        self.oas_version = oas_version
        # The number of pages in which you want to export the APIs.
        self.page_number = page_number
        self.security_token = security_token
        # The environment to which the API is published. Valid values:
        # 
        # *   **RELEASE**: the production environment
        # *   **PRE**: the pre-release environment
        # *   **TEST**: the test environment
        self.stage_name = stage_name
        # Specifies whether to export API Gateway extensions at the same time.
        self.with_xextensions = with_xextensions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id_list is not None:
            result['ApiIdList'] = self.api_id_list

        if self.data_format is not None:
            result['DataFormat'] = self.data_format

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.oas_version is not None:
            result['OasVersion'] = self.oas_version

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.with_xextensions is not None:
            result['WithXExtensions'] = self.with_xextensions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiIdList') is not None:
            self.api_id_list = m.get('ApiIdList')

        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('OasVersion') is not None:
            self.oas_version = m.get('OasVersion')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('WithXExtensions') is not None:
            self.with_xextensions = m.get('WithXExtensions')

        return self

