# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class QueryVideoAuditResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryVideoAuditResultResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务处理结果状态码
        self.code = code
        # 视频审校的详细结果
        self.data = data
        # HTTP响应状态码
        self.http_status_code = http_status_code
        # 业务处理结果描述信息
        self.message = message
        # 本次API请求的唯一标识
        self.request_id = request_id
        # 请求是否处理成功
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

        if self.message is not None:
            result['Message'] = self.message

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
            temp_model = main_models.QueryVideoAuditResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryVideoAuditResultResponseBodyData(DaraModel):
    def __init__(
        self,
        duration: float = None,
        error_message: str = None,
        fps: float = None,
        frame_audited: int = None,
        height: int = None,
        image_urls: List[main_models.QueryVideoAuditResultResponseBodyDataImageUrls] = None,
        results: List[main_models.QueryVideoAuditResultResponseBodyDataResults] = None,
        status: str = None,
        text: str = None,
        total_frame_audit: int = None,
        total_frames: int = None,
        total_shots: int = None,
        video_file_key: str = None,
        video_url: str = None,
        width: int = None,
    ):
        # 视频总时长（秒）
        self.duration = duration
        # 任务执行失败时的错误信息
        self.error_message = error_message
        # 视频帧率（FPS）
        self.fps = fps
        # 已经完成审核的帧数
        self.frame_audited = frame_audited
        # 视频高度（像素）
        self.height = height
        # 抽取的图片URL列表
        self.image_urls = image_urls
        # 图片审核结果详情
        self.results = results
        # 任务状态：PENDING(待执行)、RUNNING(执行中)、SUCCESSED(成功)、FAILED(失败)、CANCELED(取消)
        self.status = status
        # 视频审校的文本结果
        self.text = text
        # 需要审核的视频帧总数
        self.total_frame_audit = total_frame_audit
        # 视频总帧数
        self.total_frames = total_frames
        # 检测到的视频分镜总数
        self.total_shots = total_shots
        # 被审核的视频文件Key
        self.video_file_key = video_file_key
        # 被审核的视频URL地址
        self.video_url = video_url
        # 视频宽度（像素）
        self.width = width

    def validate(self):
        if self.image_urls:
            for v1 in self.image_urls:
                 if v1:
                    v1.validate()
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.frame_audited is not None:
            result['FrameAudited'] = self.frame_audited

        if self.height is not None:
            result['Height'] = self.height

        result['ImageUrls'] = []
        if self.image_urls is not None:
            for k1 in self.image_urls:
                result['ImageUrls'].append(k1.to_map() if k1 else None)

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.text is not None:
            result['Text'] = self.text

        if self.total_frame_audit is not None:
            result['TotalFrameAudit'] = self.total_frame_audit

        if self.total_frames is not None:
            result['TotalFrames'] = self.total_frames

        if self.total_shots is not None:
            result['TotalShots'] = self.total_shots

        if self.video_file_key is not None:
            result['VideoFileKey'] = self.video_file_key

        if self.video_url is not None:
            result['VideoUrl'] = self.video_url

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('FrameAudited') is not None:
            self.frame_audited = m.get('FrameAudited')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        self.image_urls = []
        if m.get('ImageUrls') is not None:
            for k1 in m.get('ImageUrls'):
                temp_model = main_models.QueryVideoAuditResultResponseBodyDataImageUrls()
                self.image_urls.append(temp_model.from_map(k1))

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.QueryVideoAuditResultResponseBodyDataResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('TotalFrameAudit') is not None:
            self.total_frame_audit = m.get('TotalFrameAudit')

        if m.get('TotalFrames') is not None:
            self.total_frames = m.get('TotalFrames')

        if m.get('TotalShots') is not None:
            self.total_shots = m.get('TotalShots')

        if m.get('VideoFileKey') is not None:
            self.video_file_key = m.get('VideoFileKey')

        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class QueryVideoAuditResultResponseBodyDataResults(DaraModel):
    def __init__(
        self,
        data_id: str = None,
        req_id: str = None,
        result: List[main_models.QueryVideoAuditResultResponseBodyDataResultsResult] = None,
        risk_level: str = None,
    ):
        # 对应图片的ID，与ImageUrl中的id字段对应
        self.data_id = data_id
        # 审核请求ID
        self.req_id = req_id
        # 图片检测的风险标签、置信分等参数结果
        self.result = result
        # 风险等级：high(高风险)、medium(中风险)、low(低风险)、none(未检测到风险)
        self.risk_level = risk_level

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
        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.req_id is not None:
            result['ReqId'] = self.req_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.QueryVideoAuditResultResponseBodyDataResultsResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class QueryVideoAuditResultResponseBodyDataResultsResult(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        label: str = None,
    ):
        # 0到100分，保留到小数点后2位，部分标签无置信分
        self.confidence = confidence
        # Label字段的解释说明
        self.description = description
        # 图片内容检测运算后返回的标签，如：nonLabel（未检测出风险）
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

class QueryVideoAuditResultResponseBodyDataImageUrls(DaraModel):
    def __init__(
        self,
        id: str = None,
        timestamp: float = None,
        url: str = None,
    ):
        # 图片ID，与AliyunImageAuditResult中的dataId对应
        self.id = id
        self.timestamp = timestamp
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

