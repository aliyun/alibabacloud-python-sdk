# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ListDataCenterTableResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListDataCenterTableResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data returned in the response.
        self.data = data
        # The code that indicates the result of the request. If the request fails, an error code is returned.
        self.error_code = error_code
        # The error message returned if the request fails.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request succeeded.
        # 
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

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
        if m.get('Data') is not None:
            temp_model = main_models.ListDataCenterTableResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDataCenterTableResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListDataCenterTableResponseBodyDataContent] = None,
        page_number: int = None,
        page_size: int = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        # A list of the data tables.
        self.content = content
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The total number of entries.
        self.total_elements = total_elements
        # The total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.ListDataCenterTableResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class ListDataCenterTableResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        desc_update_time: str = None,
        dms_db_id: int = None,
        dms_instance_id: int = None,
        gmt_created: str = None,
        import_type: str = None,
        instance_name: str = None,
        table_desc: str = None,
        table_id: str = None,
        table_name: str = None,
    ):
        # The database name.
        # 
        # - If `ImportType` is `FILE`, this parameter returns the file name.
        self.database_name = database_name
        # The time when the data table description was last updated.
        self.desc_update_time = desc_update_time
        # The ID of the DMS database.
        # 
        # - This parameter is not returned if `ImportType` is `FILE`.
        self.dms_db_id = dms_db_id
        # The ID of the DMS instance that hosts the database.
        # 
        # - This parameter is not returned if `ImportType` is `FILE`.
        self.dms_instance_id = dms_instance_id
        # The time when the data table was created.
        self.gmt_created = gmt_created
        # The import type. Valid value:
        # 
        # - **FILE**: The data is imported from a file.
        self.import_type = import_type
        # The instance name.
        # 
        # - If `ImportType` is `FILE`, this parameter returns the file ID.
        self.instance_name = instance_name
        # The description of the data table.
        self.table_desc = table_desc
        # The ID of the data table.
        self.table_id = table_id
        # The table name.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.desc_update_time is not None:
            result['DescUpdateTime'] = self.desc_update_time

        if self.dms_db_id is not None:
            result['DmsDbId'] = self.dms_db_id

        if self.dms_instance_id is not None:
            result['DmsInstanceId'] = self.dms_instance_id

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.import_type is not None:
            result['ImportType'] = self.import_type

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.table_desc is not None:
            result['TableDesc'] = self.table_desc

        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('DescUpdateTime') is not None:
            self.desc_update_time = m.get('DescUpdateTime')

        if m.get('DmsDbId') is not None:
            self.dms_db_id = m.get('DmsDbId')

        if m.get('DmsInstanceId') is not None:
            self.dms_instance_id = m.get('DmsInstanceId')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('ImportType') is not None:
            self.import_type = m.get('ImportType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('TableDesc') is not None:
            self.table_desc = m.get('TableDesc')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

