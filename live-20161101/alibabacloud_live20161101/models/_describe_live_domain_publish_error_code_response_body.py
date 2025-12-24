# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDomainPublishErrorCodeResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        real_time_code_data: List[main_models.DescribeLiveDomainPublishErrorCodeResponseBodyRealTimeCodeData] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The time granularity of the query. Unit: seconds. Default value: 60.
        self.data_interval = data_interval
        # The ingest domain.
        self.domain_name = domain_name
        # The end of the time range during which data was queried. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.end_time = end_time
        # The proportions of error codes at each time interval.
        self.real_time_code_data = real_time_code_data
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range during which data was queried. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.start_time = start_time

    def validate(self):
        if self.real_time_code_data:
            for v1 in self.real_time_code_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['RealTimeCodeData'] = []
        if self.real_time_code_data is not None:
            for k1 in self.real_time_code_data:
                result['RealTimeCodeData'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.real_time_code_data = []
        if m.get('RealTimeCodeData') is not None:
            for k1 in m.get('RealTimeCodeData'):
                temp_model = main_models.DescribeLiveDomainPublishErrorCodeResponseBodyRealTimeCodeData()
                self.real_time_code_data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeLiveDomainPublishErrorCodeResponseBodyRealTimeCodeData(DaraModel):
    def __init__(
        self,
        code_data: List[main_models.DescribeLiveDomainPublishErrorCodeResponseBodyRealTimeCodeDataCodeData] = None,
        time_stamp: str = None,
    ):
        # The proportions of error codes.
        self.code_data = code_data
        # The timestamp of the data returned.
        self.time_stamp = time_stamp

    def validate(self):
        if self.code_data:
            for v1 in self.code_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CodeData'] = []
        if self.code_data is not None:
            for k1 in self.code_data:
                result['CodeData'].append(k1.to_map() if k1 else None)

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.code_data = []
        if m.get('CodeData') is not None:
            for k1 in m.get('CodeData'):
                temp_model = main_models.DescribeLiveDomainPublishErrorCodeResponseBodyRealTimeCodeDataCodeData()
                self.code_data.append(temp_model.from_map(k1))

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

class DescribeLiveDomainPublishErrorCodeResponseBodyRealTimeCodeDataCodeData(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: str = None,
        proportion: str = None,
    ):
        # The response code. Valid values:
        # 
        # *   3: The data read timed out.
        # *   4: A data write error occurred.
        # *   6: The data write timed out.
        # *   200: The request is successful.
        # *   500: An unknown internal error occurred.
        # *   501: The stream ingest failed.
        # *   502: The signaling operation timed out.
        # *   401: A stream ingest parameter is invalid.
        # *   403: The stream ingest authentication failed.
        self.code = code
        # The number of times the HTTP status code was returned.
        self.count = count
        # The proportion of the HTTP status code.
        self.proportion = proportion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        if self.proportion is not None:
            result['Proportion'] = self.proportion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')

        return self

