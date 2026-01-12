# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetTextScanResultResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetTextScanResultResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code.
        self.code = code
        # Returned data.
        self.data = data
        # Further description of the error code.
        self.msg = msg
        # ID assigned by the backend to uniquely identify a request. It can be used for troubleshooting.
        self.request_id = request_id
        # Success indicator.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetTextScanResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTextScanResultResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.GetTextScanResultResponseBodyDataItems] = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # Current page number.
        self.current_page = current_page
        # Data for the current page.
        self.items = items
        # Page size.
        self.page_size = page_size
        # Total number of records.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.GetTextScanResultResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetTextScanResultResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        bailian_request_id: str = None,
        content: str = None,
        data_id: str = None,
        ext_feedback: str = None,
        extra: Dict[str, Any] = None,
        gmt_create: str = None,
        labels: str = None,
        request_id: str = None,
        request_time: str = None,
        result: List[main_models.GetTextScanResultResponseBodyDataItemsResult] = None,
        risk_level: str = None,
        scan_result: str = None,
        score: float = None,
        service_code: str = None,
        suggestion: str = None,
        task_id: str = None,
    ):
        self.account_id = account_id
        # Bailian Request ID
        self.bailian_request_id = bailian_request_id
        # Content.
        self.content = content
        self.data_id = data_id
        # Feedback information.
        self.ext_feedback = ext_feedback
        # Spare parameters.
        self.extra = extra
        # Creation time.
        self.gmt_create = gmt_create
        # Labels.
        self.labels = labels
        # Request ID.
        self.request_id = request_id
        # Request time.
        self.request_time = request_time
        # Detection results.
        self.result = result
        # Risk level, returned based on the set high and low risk scores. The return values include:
        # 
        # - high: High risk
        # 
        # - medium: Medium risk
        #  
        # - low: Low risk
        # 
        # - none: No risk detected
        self.risk_level = risk_level
        # Details of the result.
        self.scan_result = scan_result
        # Score.
        self.score = score
        # Service code.
        self.service_code = service_code
        # Suggestion for handling.
        self.suggestion = suggestion
        # Task ID.
        self.task_id = task_id

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.bailian_request_id is not None:
            result['BailianRequestId'] = self.bailian_request_id

        if self.content is not None:
            result['Content'] = self.content

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.ext_feedback is not None:
            result['ExtFeedback'] = self.ext_feedback

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.request_time is not None:
            result['RequestTime'] = self.request_time

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.scan_result is not None:
            result['ScanResult'] = self.scan_result

        if self.score is not None:
            result['Score'] = self.score

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('BailianRequestId') is not None:
            self.bailian_request_id = m.get('BailianRequestId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('ExtFeedback') is not None:
            self.ext_feedback = m.get('ExtFeedback')

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.GetTextScanResultResponseBodyDataItemsResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('ScanResult') is not None:
            self.scan_result = m.get('ScanResult')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class GetTextScanResultResponseBodyDataItemsResult(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        label: str = None,
    ):
        # Confidence score, ranging from 0 to 100, with two decimal places retained.
        self.confidence = confidence
        # Description.
        self.description = description
        # Label.
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

