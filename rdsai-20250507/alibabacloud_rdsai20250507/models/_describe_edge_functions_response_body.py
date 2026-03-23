# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class DescribeEdgeFunctionsResponseBody(DaraModel):
    def __init__(
        self,
        edge_functions: List[main_models.DescribeEdgeFunctionsResponseBodyEdgeFunctions] = None,
        instance_name: str = None,
        request_id: str = None,
    ):
        # The list of edge functions.
        self.edge_functions = edge_functions
        # The ID of the RDS Supabase instance.
        self.instance_name = instance_name
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.edge_functions:
            for v1 in self.edge_functions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EdgeFunctions'] = []
        if self.edge_functions is not None:
            for k1 in self.edge_functions:
                result['EdgeFunctions'].append(k1.to_map() if k1 else None)

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edge_functions = []
        if m.get('EdgeFunctions') is not None:
            for k1 in m.get('EdgeFunctions'):
                temp_model = main_models.DescribeEdgeFunctionsResponseBodyEdgeFunctions()
                self.edge_functions.append(temp_model.from_map(k1))

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEdgeFunctionsResponseBodyEdgeFunctions(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        created_time: str = None,
        edge_function_name: str = None,
        function_url: str = None,
        memory_size: str = None,
        modified_time: str = None,
        runtime: str = None,
        status: str = None,
        url_internet: str = None,
        url_intranet: str = None,
    ):
        # The number of vCPUs used by the cluster.
        self.cpu = cpu
        # The time when the function was created.
        self.created_time = created_time
        # The edge function name.
        self.edge_function_name = edge_function_name
        # The URL for accessing the function.
        self.function_url = function_url
        # The memory size. Unit: MiB.
        self.memory_size = memory_size
        # The time when the function was last created. The time is displayed in UTC.
        self.modified_time = modified_time
        # The runtime environment for the function, which includes the Linux environment and the Deno version.
        self.runtime = runtime
        # The instance status. For more information, see [Instance state table](https://help.aliyun.com/document_detail/2623972.html).
        self.status = status
        # The public URL for accessing the application.
        self.url_internet = url_internet
        # The internal URL for accessing the application.
        self.url_intranet = url_intranet

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.edge_function_name is not None:
            result['EdgeFunctionName'] = self.edge_function_name

        if self.function_url is not None:
            result['FunctionUrl'] = self.function_url

        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.runtime is not None:
            result['Runtime'] = self.runtime

        if self.status is not None:
            result['Status'] = self.status

        if self.url_internet is not None:
            result['UrlInternet'] = self.url_internet

        if self.url_intranet is not None:
            result['UrlIntranet'] = self.url_intranet

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('EdgeFunctionName') is not None:
            self.edge_function_name = m.get('EdgeFunctionName')

        if m.get('FunctionUrl') is not None:
            self.function_url = m.get('FunctionUrl')

        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UrlInternet') is not None:
            self.url_internet = m.get('UrlInternet')

        if m.get('UrlIntranet') is not None:
            self.url_intranet = m.get('UrlIntranet')

        return self

