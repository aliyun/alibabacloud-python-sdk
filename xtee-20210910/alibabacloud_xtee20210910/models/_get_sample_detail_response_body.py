# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class GetSampleDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.GetSampleDetailResponseBodyResultObject = None,
    ):
        # The status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Request result.
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
            temp_model = main_models.GetSampleDetailResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class GetSampleDetailResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        column_stats: List[main_models.GetSampleDetailResponseBodyResultObjectColumnStats] = None,
        date_type: str = None,
        download_url: str = None,
        file_name: str = None,
        file_size: int = None,
        preview_data: main_models.GetSampleDetailResponseBodyResultObjectPreviewData = None,
        remark: str = None,
        row_count: int = None,
        sample_id: int = None,
        sample_name: str = None,
        tab: str = None,
        upload_time: str = None,
        upload_user_name: str = None,
    ):
        # Columns.
        self.column_stats = column_stats
        # The time filter Type. You can filter by the last 7 Days, last 30 Days, last 6 months, or Custom.
        self.date_type = date_type
        # The download URL of the file.
        self.download_url = download_url
        # File name.  
        # > The file name must end with .txt or .sql. For example, test.txt or test.sql.
        self.file_name = file_name
        # File Size (bytes).
        self.file_size = file_size
        # Table data.
        self.preview_data = preview_data
        # Remarks.
        self.remark = remark
        # The number of result records returned.
        self.row_count = row_count
        # The sample ID.
        self.sample_id = sample_id
        # Sample name.
        self.sample_name = sample_name
        # Scenario.
        self.tab = tab
        # File upload time.
        self.upload_time = upload_time
        # Uploader.
        self.upload_user_name = upload_user_name

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
        result['ColumnStats'] = []
        if self.column_stats is not None:
            for k1 in self.column_stats:
                result['ColumnStats'].append(k1.to_map() if k1 else None)

        if self.date_type is not None:
            result['DateType'] = self.date_type

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.preview_data is not None:
            result['PreviewData'] = self.preview_data.to_map()

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.row_count is not None:
            result['RowCount'] = self.row_count

        if self.sample_id is not None:
            result['SampleId'] = self.sample_id

        if self.sample_name is not None:
            result['SampleName'] = self.sample_name

        if self.tab is not None:
            result['Tab'] = self.tab

        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time

        if self.upload_user_name is not None:
            result['UploadUserName'] = self.upload_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.column_stats = []
        if m.get('ColumnStats') is not None:
            for k1 in m.get('ColumnStats'):
                temp_model = main_models.GetSampleDetailResponseBodyResultObjectColumnStats()
                self.column_stats.append(temp_model.from_map(k1))

        if m.get('DateType') is not None:
            self.date_type = m.get('DateType')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('PreviewData') is not None:
            temp_model = main_models.GetSampleDetailResponseBodyResultObjectPreviewData()
            self.preview_data = temp_model.from_map(m.get('PreviewData'))

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')

        if m.get('SampleId') is not None:
            self.sample_id = m.get('SampleId')

        if m.get('SampleName') is not None:
            self.sample_name = m.get('SampleName')

        if m.get('Tab') is not None:
            self.tab = m.get('Tab')

        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')

        if m.get('UploadUserName') is not None:
            self.upload_user_name = m.get('UploadUserName')

        return self

class GetSampleDetailResponseBodyResultObjectPreviewData(DaraModel):
    def __init__(
        self,
        headers: List[str] = None,
        rows: List[List[str]] = None,
    ):
        # Header information returned.
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

class GetSampleDetailResponseBodyResultObjectColumnStats(DaraModel):
    def __init__(
        self,
        distinct_number: int = None,
        distinct_rate: str = None,
        field_name: str = None,
        miss_number: int = None,
        miss_rate: str = None,
        row_number: int = None,
    ):
        # De-duplication count.
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

