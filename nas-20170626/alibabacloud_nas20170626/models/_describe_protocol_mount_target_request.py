# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeProtocolMountTargetRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        file_system_id: str = None,
        filters: List[main_models.DescribeProtocolMountTargetRequestFilters] = None,
        max_results: int = None,
        next_token: str = None,
        protocol_service_ids: str = None,
    ):
        # Ensures the idempotence of the request. Generate a unique parameter value from your client to ensure that the value is unique among different requests.
        # 
        # ClientToken supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system uses the RequestId of the API request as the ClientToken. The RequestId may vary for each API request.
        self.client_token = client_token
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The filter keys for querying protocol service export directories.
        self.filters = filters
        # The maximum number of results to return per query.
        # 
        #  - Valid values: 10 to 100.
        # 
        # 
        # - Default value: 20.
        self.max_results = max_results
        # The token used to initiate the next request when the response is truncated. You can use this token to retrieve the remaining results from where the truncation occurred.
        self.next_token = next_token
        # The list of protocol service IDs.
        self.protocol_service_ids = protocol_service_ids

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.protocol_service_ids is not None:
            result['ProtocolServiceIds'] = self.protocol_service_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.DescribeProtocolMountTargetRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProtocolServiceIds') is not None:
            self.protocol_service_ids = m.get('ProtocolServiceIds')

        return self

class DescribeProtocolMountTargetRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The name of the filter key.
        # 
        # - ProtocolServiceIds: filters by protocol service ID.
        # 
        # - ExportIds: filters by export directory ID.
        # 
        # - VpcIds: filters by VPC ID.
        # 
        # - FsetIds: filters by fileset ID.
        # 
        # - Paths: filters by the file system path that corresponds to the mount target.
        # 
        # - AccessGroupNames: filters by permission group name.
        self.key = key
        # The value of the filter key. Wildcards are not supported.
        # 
        # - If Key is set to ProtocolServiceIds, set Value to a protocol service ID. You can specify up to 10 protocol service IDs. Example: `ptc-12345678` or `ptc-12345678,ptc-12345679`.
        # 
        # - If Key is set to ExportIds, set Value to an export directory ID. You can specify up to 10 export directory IDs. Example: `exp-12345678` or `exp-12345678,exp-12345679`.
        # 
        # - If Key is set to VpcIds, set Value to the VPC ID of the protocol service. You can specify up to 10 VPC IDs. Example: `vpc-12345678` or `vpc-12345678,vpc-12345679`.
        # 
        # - If Key is set to FsetIds, set Value to a fileset ID. You can specify up to 10 fileset IDs. Example: `fset-12345678` or `fset-12345678,fset-12345679`.
        # 
        # - If Key is set to Paths, set Value to the file system directory that corresponds to the mount target. You can specify up to 10 paths. Example: `/cpfs/mnt_1/` or `/cpfs/mnt_1/,/cpfs/mnt_2/`.
        # 
        # - If Key is set to AccessGroupNames, set Value to the permission group name of the protocol service. You can specify up to 10 permission group names. Example: `ag-12345678` or `ag-12345678,ag-12345679`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

