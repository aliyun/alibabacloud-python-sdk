# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListChainInstanceResponseBody(DaraModel):
    def __init__(
        self,
        chain_instances: List[main_models.ListChainInstanceResponseBodyChainInstances] = None,
        code: str = None,
        instance_id: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries to return on each page.
        self.chain_instances = chain_instances
        # The version of the delivery chain.
        self.code = code
        # The page number of the page to return.
        self.instance_id = instance_id
        # The execution record of the delivery chain.
        self.is_success = is_success
        # 30
        self.page_no = page_no
        # Indicates whether the operation is successful.
        self.page_size = page_size
        # The ID of the Container Registry instance.
        self.request_id = request_id
        # The name of the repository.
        self.total_count = total_count

    def validate(self):
        if self.chain_instances:
            for v1 in self.chain_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChainInstances'] = []
        if self.chain_instances is not None:
            for k1 in self.chain_instances:
                result['ChainInstances'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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
        self.chain_instances = []
        if m.get('ChainInstances') is not None:
            for k1 in m.get('ChainInstances'):
                temp_model = main_models.ListChainInstanceResponseBodyChainInstances()
                self.chain_instances.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

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

class ListChainInstanceResponseBodyChainInstances(DaraModel):
    def __init__(
        self,
        chain: main_models.ListChainInstanceResponseBodyChainInstancesChain = None,
        chain_instance_id: str = None,
        end_time: int = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        result: str = None,
        start_time: int = None,
        status: str = None,
    ):
        # The name of the namespace.
        self.chain = chain
        # 1
        self.chain_instance_id = chain_instance_id
        # The ID of the Container Registry instance.
        self.end_time = end_time
        # The ID of the delivery chain.
        self.repo_name = repo_name
        # The execution result of the delivery chain. Valid values:
        # 
        # *   `SUCCESS`
        # *   `FAILED`
        # *   `CANCELED`
        # *   `DENIED`
        self.repo_namespace_name = repo_namespace_name
        # The list of the execution records of delivery chains.
        self.result = result
        # test-repo
        self.start_time = start_time
        # The status of the delivery chain. Valid values:
        # 
        # *   `RUNNING`
        # *   `COMPLETE`
        # *   `CANCELING`
        # *   `CANCELED`
        self.status = status

    def validate(self):
        if self.chain:
            self.chain.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chain is not None:
            result['Chain'] = self.chain.to_map()

        if self.chain_instance_id is not None:
            result['ChainInstanceId'] = self.chain_instance_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name

        if self.result is not None:
            result['Result'] = self.result

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Chain') is not None:
            temp_model = main_models.ListChainInstanceResponseBodyChainInstancesChain()
            self.chain = temp_model.from_map(m.get('Chain'))

        if m.get('ChainInstanceId') is not None:
            self.chain_instance_id = m.get('ChainInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListChainInstanceResponseBodyChainInstancesChain(DaraModel):
    def __init__(
        self,
        chain_id: str = None,
        chain_name: str = None,
        version: int = None,
    ):
        # The name of the namespace.
        self.chain_id = chain_id
        # The number of entries returned on each page.
        self.chain_name = chain_name
        # The ID of the request.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chain_id is not None:
            result['ChainId'] = self.chain_id

        if self.chain_name is not None:
            result['ChainName'] = self.chain_name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')

        if m.get('ChainName') is not None:
            self.chain_name = m.get('ChainName')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

