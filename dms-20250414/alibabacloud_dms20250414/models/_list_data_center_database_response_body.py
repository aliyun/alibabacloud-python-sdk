# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ListDataCenterDatabaseResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDataCenterDatabaseResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListDataCenterDatabaseResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDataCenterDatabaseResponseBodyData(DaraModel):
    def __init__(
        self,
        database_desc: str = None,
        database_name: str = None,
        db_id: str = None,
        db_type: str = None,
        desc_update_time: str = None,
        dms_db_id: int = None,
        dms_instance_id: int = None,
        download_link: str = None,
        gmt_created: str = None,
        import_type: str = None,
        instance_name: str = None,
        intranet_download_link: str = None,
        is_internal: str = None,
        oss_bucket: str = None,
        size: int = None,
        use_user_oss_bucket: bool = None,
    ):
        self.database_desc = database_desc
        self.database_name = database_name
        self.db_id = db_id
        self.db_type = db_type
        self.desc_update_time = desc_update_time
        self.dms_db_id = dms_db_id
        self.dms_instance_id = dms_instance_id
        self.download_link = download_link
        self.gmt_created = gmt_created
        self.import_type = import_type
        self.instance_name = instance_name
        self.intranet_download_link = intranet_download_link
        self.is_internal = is_internal
        self.oss_bucket = oss_bucket
        self.size = size
        self.use_user_oss_bucket = use_user_oss_bucket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_desc is not None:
            result['DatabaseDesc'] = self.database_desc

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.desc_update_time is not None:
            result['DescUpdateTime'] = self.desc_update_time

        if self.dms_db_id is not None:
            result['DmsDbId'] = self.dms_db_id

        if self.dms_instance_id is not None:
            result['DmsInstanceId'] = self.dms_instance_id

        if self.download_link is not None:
            result['DownloadLink'] = self.download_link

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.import_type is not None:
            result['ImportType'] = self.import_type

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.intranet_download_link is not None:
            result['IntranetDownloadLink'] = self.intranet_download_link

        if self.is_internal is not None:
            result['IsInternal'] = self.is_internal

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.size is not None:
            result['Size'] = self.size

        if self.use_user_oss_bucket is not None:
            result['UseUserOssBucket'] = self.use_user_oss_bucket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseDesc') is not None:
            self.database_desc = m.get('DatabaseDesc')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('DescUpdateTime') is not None:
            self.desc_update_time = m.get('DescUpdateTime')

        if m.get('DmsDbId') is not None:
            self.dms_db_id = m.get('DmsDbId')

        if m.get('DmsInstanceId') is not None:
            self.dms_instance_id = m.get('DmsInstanceId')

        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('ImportType') is not None:
            self.import_type = m.get('ImportType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IntranetDownloadLink') is not None:
            self.intranet_download_link = m.get('IntranetDownloadLink')

        if m.get('IsInternal') is not None:
            self.is_internal = m.get('IsInternal')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('UseUserOssBucket') is not None:
            self.use_user_oss_bucket = m.get('UseUserOssBucket')

        return self

