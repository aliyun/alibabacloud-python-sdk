# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeExporterOutputListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        datapoints: main_models.DescribeExporterOutputListResponseBodyDatapoints = None,
        message: str = None,
        page_number: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # The HTTP status code.
        # 
        # > The status code 200 indicates that the request was successful. Other status codes indicate that the request failed.
        self.code = code
        # The configuration sets for exporting monitoring data.
        self.datapoints = datapoints
        # The returned message.
        self.message = message
        # The page number of the returned page.
        self.page_number = page_number
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.success = success
        # The total number of returned entries.
        self.total = total

    def validate(self):
        if self.datapoints:
            self.datapoints.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.datapoints is not None:
            result['Datapoints'] = self.datapoints.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Datapoints') is not None:
            temp_model = main_models.DescribeExporterOutputListResponseBodyDatapoints()
            self.datapoints = temp_model.from_map(m.get('Datapoints'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeExporterOutputListResponseBodyDatapoints(DaraModel):
    def __init__(
        self,
        datapoint: List[main_models.DescribeExporterOutputListResponseBodyDatapointsDatapoint] = None,
    ):
        self.datapoint = datapoint

    def validate(self):
        if self.datapoint:
            for v1 in self.datapoint:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Datapoint'] = []
        if self.datapoint is not None:
            for k1 in self.datapoint:
                result['Datapoint'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.datapoint = []
        if m.get('Datapoint') is not None:
            for k1 in m.get('Datapoint'):
                temp_model = main_models.DescribeExporterOutputListResponseBodyDatapointsDatapoint()
                self.datapoint.append(temp_model.from_map(k1))

        return self

class DescribeExporterOutputListResponseBodyDatapointsDatapoint(DaraModel):
    def __init__(
        self,
        config_json: main_models.DescribeExporterOutputListResponseBodyDatapointsDatapointConfigJson = None,
        create_time: int = None,
        dest_name: str = None,
        dest_type: str = None,
    ):
        # The JSON object that contains the details about the destination to which the monitoring data is exported.
        self.config_json = config_json
        # The time when the configuration set was created. The value is a UNIX timestamp.
        self.create_time = create_time
        # The name of the configuration set.
        self.dest_name = dest_name
        # The service to which the monitoring data is exported.
        # 
        # > Only Log Service is supported. More services will be supported in the future.
        self.dest_type = dest_type

    def validate(self):
        if self.config_json:
            self.config_json.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_json is not None:
            result['ConfigJson'] = self.config_json.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dest_name is not None:
            result['DestName'] = self.dest_name

        if self.dest_type is not None:
            result['DestType'] = self.dest_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigJson') is not None:
            temp_model = main_models.DescribeExporterOutputListResponseBodyDatapointsDatapointConfigJson()
            self.config_json = temp_model.from_map(m.get('ConfigJson'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DestName') is not None:
            self.dest_name = m.get('DestName')

        if m.get('DestType') is not None:
            self.dest_type = m.get('DestType')

        return self

class DescribeExporterOutputListResponseBodyDatapointsDatapointConfigJson(DaraModel):
    def __init__(
        self,
        ak: str = None,
        endpoint: str = None,
        logstore: str = None,
        project: str = None,
    ):
        # The AccessKey ID.
        self.ak = ak
        # The Log Service endpoint to which the monitoring data is exported.
        self.endpoint = endpoint
        # The Logstore.
        self.logstore = logstore
        # The Log Service project to which the monitoring data is exported.
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ak is not None:
            result['ak'] = self.ak

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.project is not None:
            result['project'] = self.project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ak') is not None:
            self.ak = m.get('ak')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('project') is not None:
            self.project = m.get('project')

        return self

