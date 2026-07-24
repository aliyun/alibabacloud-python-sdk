# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetScanResultResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetScanResultResponseBodyData = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code, which is consistent with the HTTP status code.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The further description of the error code.
        self.msg = msg
        # The ID assigned by the backend that uniquely identifies a request. You can use this ID for troubleshooting.
        self.request_id = request_id
        # The success flag.
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.GetScanResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetScanResultResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.GetScanResultResponseBodyDataItems] = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The data on the current page.
        self.items = items
        # The number of entries per page.
        self.page_size = page_size
        # The total number of records.
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
                temp_model = main_models.GetScanResultResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetScanResultResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        api_labels: str = None,
        api_request_time: str = None,
        api_risk_level: str = None,
        api_service: str = None,
        api_task_id: str = None,
        app_id: str = None,
        attack_level: str = None,
        bailian_request_id: str = None,
        content: str = None,
        data_id: str = None,
        end_time: str = None,
        ext: str = None,
        ext_feedback: str = None,
        extra: Dict[str, Any] = None,
        frame_count: int = None,
        gmt_create: str = None,
        guard_file_urls: List[str] = None,
        guard_image_urls: List[str] = None,
        image_labels: List[Dict[str, Any]] = None,
        image_service: str = None,
        image_url: str = None,
        image_urls: List[str] = None,
        labels: str = None,
        live_id: str = None,
        malicious_file_level: str = None,
        malicious_url_level: str = None,
        manual_only: bool = None,
        no_labels: List[str] = None,
        offset: int = None,
        page_num: int = None,
        request_from: str = None,
        request_id: str = None,
        request_time: str = None,
        resource_type: str = None,
        result: List[main_models.GetScanResultResponseBodyDataItemsResult] = None,
        review_labels: str = None,
        review_risk_level: str = None,
        review_time: str = None,
        review_uid: str = None,
        reviewed: bool = None,
        risk_level: str = None,
        risk_tips: str = None,
        risk_words: str = None,
        scan_result: str = None,
        score: float = None,
        sensitive_level: str = None,
        service_code: str = None,
        start_time: str = None,
        suggestion: str = None,
        task_id: str = None,
        text_labels: List[Dict[str, Any]] = None,
        thumbnail: str = None,
        time_stamp: str = None,
        url: str = None,
        voice_labels: List[Dict[str, Any]] = None,
        voice_scan_opened: bool = None,
        voice_service: str = None,
    ):
        # The AccountId input parameter from the customer.
        self.account_id = account_id
        # The machine-assisted moderation labels.
        self.api_labels = api_labels
        # The machine-assisted moderation time. The value is a Unix/POSIX timestamp in milliseconds.
        self.api_request_time = api_request_time
        # The machine-assisted moderation risk level.
        self.api_risk_level = api_risk_level
        # The machine-assisted moderation service.
        self.api_service = api_service
        # The machine-assisted moderation task ID.
        self.api_task_id = api_task_id
        # appId
        self.app_id = app_id
        # The attack level, returned based on the configured risk score thresholds. Valid values:
        # 
        # - high: high risk.
        # 
        # - medium: medium risk.
        #  
        # - low: low risk.
        # 
        # - none: no risk detected.
        self.attack_level = attack_level
        # The Bailian request ID.
        self.bailian_request_id = bailian_request_id
        # The content.
        self.content = content
        # dataId
        self.data_id = data_id
        # The segment end time, in seconds.
        self.end_time = end_time
        # The extended information.
        self.ext = ext
        # The feedback information.
        self.ext_feedback = ext_feedback
        # The reserved parameter.
        self.extra = extra
        # The frame count.
        self.frame_count = frame_count
        # The creation time. Format: YYYY-MM-DD HH:mm:ss.
        self.gmt_create = gmt_create
        # The multimodal file URLs.
        self.guard_file_urls = guard_file_urls
        # The multimodal image URLs.
        self.guard_image_urls = guard_image_urls
        # The image labels.
        self.image_labels = image_labels
        # The image service.
        self.image_service = image_service
        # url
        self.image_url = image_url
        # imageUrls
        self.image_urls = image_urls
        # The labels.
        self.labels = labels
        # The LiveId input parameter from the customer.
        self.live_id = live_id
        # The risk level of the malicious file.
        self.malicious_file_level = malicious_file_level
        # The risk level of the malicious URL.
        self.malicious_url_level = malicious_url_level
        # Indicates whether only manual review is used.
        self.manual_only = manual_only
        # No labels.
        self.no_labels = no_labels
        # The frame capture offset value.
        self.offset = offset
        # The page number.
        self.page_num = page_num
        # The request source.
        self.request_from = request_from
        # The request ID.
        self.request_id = request_id
        # The request time. Format: YYYY-MM-DD HH:mm:ss.
        self.request_time = request_time
        # The resource type.
        self.resource_type = resource_type
        # The result set.
        self.result = result
        # The review labels.
        self.review_labels = review_labels
        # The review status.
        self.review_risk_level = review_risk_level
        # The review time. The value is a Unix/POSIX timestamp in milliseconds.
        self.review_time = review_time
        # The reviewer.
        self.review_uid = review_uid
        # Indicates whether the content has been reviewed.
        self.reviewed = reviewed
        # The risk level, returned based on the configured risk score thresholds. Valid values:
        # 
        # - high: high risk.
        # 
        # - medium: medium risk.
        #  
        # - low: low risk.
        # 
        # - none: no risk detected.
        self.risk_level = risk_level
        # The details of the matched risk.
        self.risk_tips = risk_tips
        # The matched risk keywords.
        self.risk_words = risk_words
        # The result details.
        self.scan_result = scan_result
        # The score.
        self.score = score
        # The sensitivity level, returned based on the configured risk score thresholds. Valid values:
        # - **S1**: Low sensitivity.
        # - **S2**: Medium sensitivity.
        # - **S3**: Moderately high sensitivity.
        # - **S4**: High sensitivity.
        # - **S0**: Not sensitive.
        self.sensitive_level = sensitive_level
        # The service code.
        self.service_code = service_code
        # The segment start time, in seconds.
        self.start_time = start_time
        # The suggestion.
        self.suggestion = suggestion
        # The task ID.
        self.task_id = task_id
        # The text labels.
        self.text_labels = text_labels
        # The thumbnail URL.
        self.thumbnail = thumbnail
        # The timestamp.
        self.time_stamp = time_stamp
        # The task URL.
        self.url = url
        # The audio labels.
        self.voice_labels = voice_labels
        # Indicates whether audio detection is enabled.
        self.voice_scan_opened = voice_scan_opened
        # The audio service.
        self.voice_service = voice_service

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

        if self.api_labels is not None:
            result['ApiLabels'] = self.api_labels

        if self.api_request_time is not None:
            result['ApiRequestTime'] = self.api_request_time

        if self.api_risk_level is not None:
            result['ApiRiskLevel'] = self.api_risk_level

        if self.api_service is not None:
            result['ApiService'] = self.api_service

        if self.api_task_id is not None:
            result['ApiTaskId'] = self.api_task_id

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.attack_level is not None:
            result['AttackLevel'] = self.attack_level

        if self.bailian_request_id is not None:
            result['BailianRequestId'] = self.bailian_request_id

        if self.content is not None:
            result['Content'] = self.content

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ext is not None:
            result['Ext'] = self.ext

        if self.ext_feedback is not None:
            result['ExtFeedback'] = self.ext_feedback

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.frame_count is not None:
            result['FrameCount'] = self.frame_count

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.guard_file_urls is not None:
            result['GuardFileUrls'] = self.guard_file_urls

        if self.guard_image_urls is not None:
            result['GuardImageUrls'] = self.guard_image_urls

        if self.image_labels is not None:
            result['ImageLabels'] = self.image_labels

        if self.image_service is not None:
            result['ImageService'] = self.image_service

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.live_id is not None:
            result['LiveId'] = self.live_id

        if self.malicious_file_level is not None:
            result['MaliciousFileLevel'] = self.malicious_file_level

        if self.malicious_url_level is not None:
            result['MaliciousUrlLevel'] = self.malicious_url_level

        if self.manual_only is not None:
            result['ManualOnly'] = self.manual_only

        if self.no_labels is not None:
            result['NoLabels'] = self.no_labels

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.request_from is not None:
            result['RequestFrom'] = self.request_from

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.request_time is not None:
            result['RequestTime'] = self.request_time

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.review_labels is not None:
            result['ReviewLabels'] = self.review_labels

        if self.review_risk_level is not None:
            result['ReviewRiskLevel'] = self.review_risk_level

        if self.review_time is not None:
            result['ReviewTime'] = self.review_time

        if self.review_uid is not None:
            result['ReviewUid'] = self.review_uid

        if self.reviewed is not None:
            result['Reviewed'] = self.reviewed

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.risk_tips is not None:
            result['RiskTips'] = self.risk_tips

        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words

        if self.scan_result is not None:
            result['ScanResult'] = self.scan_result

        if self.score is not None:
            result['Score'] = self.score

        if self.sensitive_level is not None:
            result['SensitiveLevel'] = self.sensitive_level

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.text_labels is not None:
            result['TextLabels'] = self.text_labels

        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.url is not None:
            result['Url'] = self.url

        if self.voice_labels is not None:
            result['VoiceLabels'] = self.voice_labels

        if self.voice_scan_opened is not None:
            result['VoiceScanOpened'] = self.voice_scan_opened

        if self.voice_service is not None:
            result['VoiceService'] = self.voice_service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ApiLabels') is not None:
            self.api_labels = m.get('ApiLabels')

        if m.get('ApiRequestTime') is not None:
            self.api_request_time = m.get('ApiRequestTime')

        if m.get('ApiRiskLevel') is not None:
            self.api_risk_level = m.get('ApiRiskLevel')

        if m.get('ApiService') is not None:
            self.api_service = m.get('ApiService')

        if m.get('ApiTaskId') is not None:
            self.api_task_id = m.get('ApiTaskId')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AttackLevel') is not None:
            self.attack_level = m.get('AttackLevel')

        if m.get('BailianRequestId') is not None:
            self.bailian_request_id = m.get('BailianRequestId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        if m.get('ExtFeedback') is not None:
            self.ext_feedback = m.get('ExtFeedback')

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('FrameCount') is not None:
            self.frame_count = m.get('FrameCount')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GuardFileUrls') is not None:
            self.guard_file_urls = m.get('GuardFileUrls')

        if m.get('GuardImageUrls') is not None:
            self.guard_image_urls = m.get('GuardImageUrls')

        if m.get('ImageLabels') is not None:
            self.image_labels = m.get('ImageLabels')

        if m.get('ImageService') is not None:
            self.image_service = m.get('ImageService')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')

        if m.get('MaliciousFileLevel') is not None:
            self.malicious_file_level = m.get('MaliciousFileLevel')

        if m.get('MaliciousUrlLevel') is not None:
            self.malicious_url_level = m.get('MaliciousUrlLevel')

        if m.get('ManualOnly') is not None:
            self.manual_only = m.get('ManualOnly')

        if m.get('NoLabels') is not None:
            self.no_labels = m.get('NoLabels')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('RequestFrom') is not None:
            self.request_from = m.get('RequestFrom')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.GetScanResultResponseBodyDataItemsResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('ReviewLabels') is not None:
            self.review_labels = m.get('ReviewLabels')

        if m.get('ReviewRiskLevel') is not None:
            self.review_risk_level = m.get('ReviewRiskLevel')

        if m.get('ReviewTime') is not None:
            self.review_time = m.get('ReviewTime')

        if m.get('ReviewUid') is not None:
            self.review_uid = m.get('ReviewUid')

        if m.get('Reviewed') is not None:
            self.reviewed = m.get('Reviewed')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RiskTips') is not None:
            self.risk_tips = m.get('RiskTips')

        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')

        if m.get('ScanResult') is not None:
            self.scan_result = m.get('ScanResult')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('SensitiveLevel') is not None:
            self.sensitive_level = m.get('SensitiveLevel')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TextLabels') is not None:
            self.text_labels = m.get('TextLabels')

        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('VoiceLabels') is not None:
            self.voice_labels = m.get('VoiceLabels')

        if m.get('VoiceScanOpened') is not None:
            self.voice_scan_opened = m.get('VoiceScanOpened')

        if m.get('VoiceService') is not None:
            self.voice_service = m.get('VoiceService')

        return self

class GetScanResultResponseBodyDataItemsResult(DaraModel):
    def __init__(
        self,
        confidence: str = None,
        description: str = None,
        label: str = None,
    ):
        # The confidence score, ranging from 0 to 100, rounded to two decimal places.
        self.confidence = confidence
        # The description of the Label field.
        self.description = description
        # The labels.
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

