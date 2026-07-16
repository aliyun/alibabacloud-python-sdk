# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class UploadSampleFileResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.UploadSampleFileResponseBodyResultObject = None,
    ):
        # Status code.
        self.code = code
        # HTTP status code.
        self.http_status_code = http_status_code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Return Result.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.UploadSampleFileResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class UploadSampleFileResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        beyond_backtracking_period_num: int = None,
        column_stats: List[main_models.UploadSampleFileResponseBodyResultObjectColumnStats] = None,
        date_type: str = None,
        file_name: str = None,
        file_size: int = None,
        file_url: str = None,
        not_exist_scenes: List[str] = None,
        phone_invalid_list: List[str] = None,
        preview_data: main_models.UploadSampleFileResponseBodyResultObjectPreviewData = None,
        row_count: int = None,
    ):
        # Number of jobs.
        self.beyond_backtracking_period_num = beyond_backtracking_period_num
        # Columns.
        self.column_stats = column_stats
        # Time type.
        self.date_type = date_type
        # File name.
        self.file_name = file_name
        # File Size.
        self.file_size = file_size
        # File URL.
        self.file_url = file_url
        # Non-existent scenarios.
        self.not_exist_scenes = not_exist_scenes
        # Number.
        self.phone_invalid_list = phone_invalid_list
        # Table data.
        self.preview_data = preview_data
        # Number of rows.
        self.row_count = row_count

    def validate(self):
        if self.column_stats:
            for v1 in self.column_stats:
                 if v1:
                    v1.validate()
        if self.preview_data:
            self.preview_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.beyond_backtracking_period_num is not None:
            result['BeyondBacktrackingPeriodNum'] = self.beyond_backtracking_period_num

        result['ColumnStats'] = []
        if self.column_stats is not None:
            for k1 in self.column_stats:
                result['ColumnStats'].append(k1.to_map() if k1 else None)

        if self.date_type is not None:
            result['DateType'] = self.date_type

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.not_exist_scenes is not None:
            result['NotExistScenes'] = self.not_exist_scenes

        if self.phone_invalid_list is not None:
            result['PhoneInvalidList'] = self.phone_invalid_list

        if self.preview_data is not None:
            result['PreviewData'] = self.preview_data.to_map()

        if self.row_count is not None:
            result['RowCount'] = self.row_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeyondBacktrackingPeriodNum') is not None:
            self.beyond_backtracking_period_num = m.get('BeyondBacktrackingPeriodNum')

        self.column_stats = []
        if m.get('ColumnStats') is not None:
            for k1 in m.get('ColumnStats'):
                temp_model = main_models.UploadSampleFileResponseBodyResultObjectColumnStats()
                self.column_stats.append(temp_model.from_map(k1))

        if m.get('DateType') is not None:
            self.date_type = m.get('DateType')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('NotExistScenes') is not None:
            self.not_exist_scenes = m.get('NotExistScenes')

        if m.get('PhoneInvalidList') is not None:
            self.phone_invalid_list = m.get('PhoneInvalidList')

        if m.get('PreviewData') is not None:
            temp_model = main_models.UploadSampleFileResponseBodyResultObjectPreviewData()
            self.preview_data = temp_model.from_map(m.get('PreviewData'))

        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')

        return self

class UploadSampleFileResponseBodyResultObjectPreviewData(DaraModel):
    def __init__(
        self,
        headers: List[str] = None,
        rows: List[List[str]] = None,
    ):
        # Table header.
        self.headers = headers
        # Row data.
        self.rows = rows

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['Headers'] = self.headers

        if self.rows is not None:
            result['Rows'] = self.rows

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')

        if m.get('Rows') is not None:
            self.rows = m.get('Rows')

        return self

class UploadSampleFileResponseBodyResultObjectColumnStats(DaraModel):
    def __init__(
        self,
        distinct_number: int = None,
        distinct_rate: str = None,
        field_name: str = None,
        miss_number: int = None,
        miss_rate: str = None,
        row_number: int = None,
    ):
        # De-duplication Count.
        self.distinct_number = distinct_number
        # De-duplication rate.
        self.distinct_rate = distinct_rate
        # Field Name.
        self.field_name = field_name
        # Number of missing values.
        self.miss_number = miss_number
        # Missing rate.
        self.miss_rate = miss_rate
        # Row number of the record.
        self.row_number = row_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.distinct_number is not None:
            result['DistinctNumber'] = self.distinct_number

        if self.distinct_rate is not None:
            result['DistinctRate'] = self.distinct_rate

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.miss_number is not None:
            result['MissNumber'] = self.miss_number

        if self.miss_rate is not None:
            result['MissRate'] = self.miss_rate

        if self.row_number is not None:
            result['RowNumber'] = self.row_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistinctNumber') is not None:
            self.distinct_number = m.get('DistinctNumber')

        if m.get('DistinctRate') is not None:
            self.distinct_rate = m.get('DistinctRate')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('MissNumber') is not None:
            self.miss_number = m.get('MissNumber')

        if m.get('MissRate') is not None:
            self.miss_rate = m.get('MissRate')

        if m.get('RowNumber') is not None:
            self.row_number = m.get('RowNumber')

        return self

