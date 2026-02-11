# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class ListImportedLogsByProdResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListImportedLogsByProdResponseBodyData] = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListImportedLogsByProdResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListImportedLogsByProdResponseBodyData(DaraModel):
    def __init__(
        self,
        auto_imported: int = None,
        cloud_code: str = None,
        imported: int = None,
        imported_user_count: int = None,
        log_code: str = None,
        log_mds_code: str = None,
        log_type: int = None,
        modify_time: str = None,
        prod_code: str = None,
        total_user_count: int = None,
        un_imported_user_count: int = None,
    ):
        # Indicates whether the log is automatically added to the threat analysis feature within newly added accounts. Valid values:
        # 
        # *   1: yes.
        # *   0: no.
        self.auto_imported = auto_imported
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud.
        # *   aliyun: Alibaba Cloud.
        # *   hcloud: Huawei Cloud.
        self.cloud_code = cloud_code
        # Indicates whether the log is added to the threat analysis feature. Valid values:
        # 
        # *   1: yes.
        # *   0: no.
        self.imported = imported
        # The number of users who have added the log.
        self.imported_user_count = imported_user_count
        # The code of the log.
        self.log_code = log_code
        # The display code of the log.
        self.log_mds_code = log_mds_code
        # The type of log. Valid values:
        #  - 1: the log produced by other product
        #  - 2: the predefined log
        #  - 3: the custom log
        self.log_type = log_type
        # The time when the log was last added.
        self.modify_time = modify_time
        # The code of the cloud service to which the log belongs.
        self.prod_code = prod_code
        # The total number of users who have the log.
        self.total_user_count = total_user_count
        # The number of users who have not added the log.
        self.un_imported_user_count = un_imported_user_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_imported is not None:
            result['AutoImported'] = self.auto_imported

        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code

        if self.imported is not None:
            result['Imported'] = self.imported

        if self.imported_user_count is not None:
            result['ImportedUserCount'] = self.imported_user_count

        if self.log_code is not None:
            result['LogCode'] = self.log_code

        if self.log_mds_code is not None:
            result['LogMdsCode'] = self.log_mds_code

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code

        if self.total_user_count is not None:
            result['TotalUserCount'] = self.total_user_count

        if self.un_imported_user_count is not None:
            result['UnImportedUserCount'] = self.un_imported_user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoImported') is not None:
            self.auto_imported = m.get('AutoImported')

        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('Imported') is not None:
            self.imported = m.get('Imported')

        if m.get('ImportedUserCount') is not None:
            self.imported_user_count = m.get('ImportedUserCount')

        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')

        if m.get('LogMdsCode') is not None:
            self.log_mds_code = m.get('LogMdsCode')

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')

        if m.get('TotalUserCount') is not None:
            self.total_user_count = m.get('TotalUserCount')

        if m.get('UnImportedUserCount') is not None:
            self.un_imported_user_count = m.get('UnImportedUserCount')

        return self

