# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListChainResponseBody(DaraModel):
    def __init__(
        self,
        chains: List[main_models.ListChainResponseBodyChains] = None,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of delivery chains.
        self.chains = chains
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The page number of the returned page.
        self.page_no = page_no
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of delivery chains.
        self.total_count = total_count

    def validate(self):
        if self.chains:
            for v1 in self.chains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Chains'] = []
        if self.chains is not None:
            for k1 in self.chains:
                result['Chains'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chains = []
        if m.get('Chains') is not None:
            for k1 in m.get('Chains'):
                temp_model = main_models.ListChainResponseBodyChains()
                self.chains.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListChainResponseBodyChains(DaraModel):
    def __init__(
        self,
        chain_id: str = None,
        create_time: int = None,
        description: str = None,
        instance_id: str = None,
        modified_time: int = None,
        name: str = None,
        scope_exclude: List[str] = None,
        scope_id: str = None,
        scope_type: str = None,
    ):
        # The ID of the delivery chain.
        self.chain_id = chain_id
        # The time when the delivery chain was created.
        self.create_time = create_time
        # The description of the delivery chain.
        self.description = description
        # The ID of the instance.
        self.instance_id = instance_id
        # The time when the delivery chain was last modified.
        self.modified_time = modified_time
        # The name of the delivery chain.
        self.name = name
        # Repositories to which the delivery chain does not apply.
        self.scope_exclude = scope_exclude
        # The ID of the delivery chain scope.
        self.scope_id = scope_id
        # The type of the delivery chain scope.
        self.scope_type = scope_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chain_id is not None:
            result['ChainId'] = self.chain_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.scope_exclude is not None:
            result['ScopeExclude'] = self.scope_exclude

        if self.scope_id is not None:
            result['ScopeId'] = self.scope_id

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ScopeExclude') is not None:
            self.scope_exclude = m.get('ScopeExclude')

        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        return self

