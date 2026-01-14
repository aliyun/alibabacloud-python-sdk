# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeDataLimitDetailResponseBody(DaraModel):
    def __init__(
        self,
        data_limit: main_models.DescribeDataLimitDetailResponseBodyDataLimit = None,
        request_id: str = None,
    ):
        # The details of the data asset.
        self.data_limit = data_limit
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data_limit:
            self.data_limit.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_limit is not None:
            result['DataLimit'] = self.data_limit.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataLimit') is not None:
            temp_model = main_models.DescribeDataLimitDetailResponseBodyDataLimit()
            self.data_limit = temp_model.from_map(m.get('DataLimit'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDataLimitDetailResponseBodyDataLimit(DaraModel):
    def __init__(
        self,
        check_status: int = None,
        check_status_name: str = None,
        gmt_create: int = None,
        id: int = None,
        local_name: str = None,
        parent_id: str = None,
        port: int = None,
        region_id: str = None,
        resource_type: int = None,
        resource_type_code: str = None,
        user_name: str = None,
    ):
        # The status of the connectivity test between the data asset and DSC. Valid values:
        # 
        # *   **2**: indicates that the data asset was being connected.
        # *   **3**: indicates that the data asset was connected to DSC.
        # *   **4**: indicates that the data asset failed to be connected.
        self.check_status = check_status
        # The result that indicates the status of the connectivity test between the data asset and DSC. Valid values:
        # 
        # *   **Passed**
        # *   **Failed**
        # *   **Testing**
        self.check_status_name = check_status_name
        # The time when the data asset was connected to DSC. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The ID of the data asset.
        self.id = id
        # The region in which the data asset resides.
        self.local_name = local_name
        # The ID and name of the data asset in the service to which the data asset belongs.
        self.parent_id = parent_id
        # The port number that is used to connect to the database.
        self.port = port
        # The ID of the region in which the data asset resides.
        self.region_id = region_id
        # The type of the service to which the data asset belongs. Valid values:
        # 
        # *   **1**: MaxCompute
        # *   **2**: OSS
        # *   **3**: AnalyticDB for MySQL
        # *   **4**: Tablestore
        # *   **5**: ApsaraDB RDS
        self.resource_type = resource_type
        # The service to which the data asset belongs. Valid values:
        # 
        # *   **MaxCompute**
        # *   **OSS**
        # *   **ADS**
        # *   **OTS**
        # *   **RDS**
        self.resource_type_code = resource_type_code
        # The account of the user who manages the data asset.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status

        if self.check_status_name is not None:
            result['CheckStatusName'] = self.check_status_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.id is not None:
            result['Id'] = self.id

        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.resource_type_code is not None:
            result['ResourceTypeCode'] = self.resource_type_code

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')

        if m.get('CheckStatusName') is not None:
            self.check_status_name = m.get('CheckStatusName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ResourceTypeCode') is not None:
            self.resource_type_code = m.get('ResourceTypeCode')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

