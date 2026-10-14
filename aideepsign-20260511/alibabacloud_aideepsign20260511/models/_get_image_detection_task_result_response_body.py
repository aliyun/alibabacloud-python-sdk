# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aideepsign20260511 import models as main_models
from darabonba.model import DaraModel

class GetImageDetectionTaskResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        detect_mode: str = None,
        http_status_code: int = None,
        labels: List[main_models.GetImageDetectionTaskResultResponseBodyLabels] = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
        tamper: main_models.GetImageDetectionTaskResultResponseBodyTamper = None,
        task_id: str = None,
    ):
        # The business error code. The value "OK" is returned when the request succeeds.
        self.code = code
        # The detection mode that was actually executed. Valid values:
        # - aigc: AIGC only.
        # - tamper: tamper detection.
        # 
        # This field is returned only when Status is succeeded.
        self.detect_mode = detect_mode
        # The HTTP status code. The value 200 is returned when the request succeeds.
        self.http_status_code = http_status_code
        # The list of detection result labels. This field is returned only when Status is succeeded and AIGC detection is included. The label values and confidence ranges vary depending on DetectMode. In aigc mode, AIGC generation identification labels are returned (see the table below). In tamper mode, aigc/aips labels are returned (confidence range: 0 to 1).
        self.labels = labels
        # The additional information. The value "success" is returned when the request succeeds. The error message is returned when the task fails. This field is returned only when Status is failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The task status. Valid values:
        # - pending: waiting.
        # - running: in progress.
        # - succeeded: completed.
        # - failed: failed.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success
        # The tamper detection result.
        self.tamper = tamper
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.tamper:
            self.tamper.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.detect_mode is not None:
            result['DetectMode'] = self.detect_mode

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        if self.tamper is not None:
            result['Tamper'] = self.tamper.to_map()

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DetectMode') is not None:
            self.detect_mode = m.get('DetectMode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.GetImageDetectionTaskResultResponseBodyLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Tamper') is not None:
            temp_model = main_models.GetImageDetectionTaskResultResponseBodyTamper()
            self.tamper = temp_model.from_map(m.get('Tamper'))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class GetImageDetectionTaskResultResponseBodyTamper(DaraModel):
    def __init__(
        self,
        ai_watermark: str = None,
        base_results: main_models.GetImageDetectionTaskResultResponseBodyTamperBaseResults = None,
        final_conclusion: str = None,
        llm_result: str = None,
        metadata_ai_flag: str = None,
        metadata_ai_source: str = None,
        risk_level: str = None,
    ):
        # The AI visible watermark. This field is returned only in large model mode. It is empty in small model mode.
        self.ai_watermark = ai_watermark
        # The basic algorithm detection results, including multi-dimensional detection scores and risk labels.
        self.base_results = base_results
        # The final conclusion.
        self.final_conclusion = final_conclusion
        # The comprehensive analysis result from the large language model.
        self.llm_result = llm_result
        # The metadata AI flag. This field is always returned.
        self.metadata_ai_flag = metadata_ai_flag
        # The source of the metadata AI flag. This field is returned only in large model mode. It is empty in small model mode.
        self.metadata_ai_source = metadata_ai_source
        # The determination result. This field is always returned.
        self.risk_level = risk_level

    def validate(self):
        if self.base_results:
            self.base_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_watermark is not None:
            result['AiWatermark'] = self.ai_watermark

        if self.base_results is not None:
            result['BaseResults'] = self.base_results.to_map()

        if self.final_conclusion is not None:
            result['FinalConclusion'] = self.final_conclusion

        if self.llm_result is not None:
            result['LlmResult'] = self.llm_result

        if self.metadata_ai_flag is not None:
            result['MetadataAiFlag'] = self.metadata_ai_flag

        if self.metadata_ai_source is not None:
            result['MetadataAiSource'] = self.metadata_ai_source

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiWatermark') is not None:
            self.ai_watermark = m.get('AiWatermark')

        if m.get('BaseResults') is not None:
            temp_model = main_models.GetImageDetectionTaskResultResponseBodyTamperBaseResults()
            self.base_results = temp_model.from_map(m.get('BaseResults'))

        if m.get('FinalConclusion') is not None:
            self.final_conclusion = m.get('FinalConclusion')

        if m.get('LlmResult') is not None:
            self.llm_result = m.get('LlmResult')

        if m.get('MetadataAiFlag') is not None:
            self.metadata_ai_flag = m.get('MetadataAiFlag')

        if m.get('MetadataAiSource') is not None:
            self.metadata_ai_source = m.get('MetadataAiSource')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class GetImageDetectionTaskResultResponseBodyTamperBaseResults(DaraModel):
    def __init__(
        self,
        aigc: main_models.GetImageDetectionTaskResultResponseBodyTamperBaseResultsAigc = None,
        aips: main_models.GetImageDetectionTaskResultResponseBodyTamperBaseResultsAips = None,
        img_type: str = None,
        ps_loc: main_models.GetImageDetectionTaskResultResponseBodyTamperBaseResultsPsLoc = None,
        recap: main_models.GetImageDetectionTaskResultResponseBodyTamperBaseResultsRecap = None,
    ):
        # The AIGC detection result.
        self.aigc = aigc
        # The AI post-processing detection score.
        self.aips = aips
        # The image type.
        self.img_type = img_type
        # The PS tamper localization result.
        self.ps_loc = ps_loc
        # The recapture/copy detection result.
        self.recap = recap

    def validate(self):
        if self.aigc:
            self.aigc.validate()
        if self.aips:
            self.aips.validate()
        if self.ps_loc:
            self.ps_loc.validate()
        if self.recap:
            self.recap.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aigc is not None:
            result['Aigc'] = self.aigc.to_map()

        if self.aips is not None:
            result['Aips'] = self.aips.to_map()

        if self.img_type is not None:
            result['ImgType'] = self.img_type

        if self.ps_loc is not None:
            result['PsLoc'] = self.ps_loc.to_map()

        if self.recap is not None:
            result['Recap'] = self.recap.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aigc') is not None:
            temp_model = main_models.GetImageDetectionTaskResultResponseBodyTamperBaseResultsAigc()
            self.aigc = temp_model.from_map(m.get('Aigc'))

        if m.get('Aips') is not None:
            temp_model = main_models.GetImageDetectionTaskResultResponseBodyTamperBaseResultsAips()
            self.aips = temp_model.from_map(m.get('Aips'))

        if m.get('ImgType') is not None:
            self.img_type = m.get('ImgType')

        if m.get('PsLoc') is not None:
            temp_model = main_models.GetImageDetectionTaskResultResponseBodyTamperBaseResultsPsLoc()
            self.ps_loc = temp_model.from_map(m.get('PsLoc'))

        if m.get('Recap') is not None:
            temp_model = main_models.GetImageDetectionTaskResultResponseBodyTamperBaseResultsRecap()
            self.recap = temp_model.from_map(m.get('Recap'))

        return self

class GetImageDetectionTaskResultResponseBodyTamperBaseResultsRecap(DaraModel):
    def __init__(
        self,
        desc: str = None,
        risk: str = None,
        score: float = None,
    ):
        # The recapture/copy detection result description.
        self.desc = desc
        # The recapture/copy dimension risk label.
        self.risk = risk
        # The recapture/copy detection score. Value range: 0 to 1. A higher value indicates a greater likelihood of recapture or copying.
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.risk is not None:
            result['Risk'] = self.risk

        if self.score is not None:
            result['Score'] = self.score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Risk') is not None:
            self.risk = m.get('Risk')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        return self

class GetImageDetectionTaskResultResponseBodyTamperBaseResultsPsLoc(DaraModel):
    def __init__(
        self,
        desc: str = None,
        items: List[main_models.GetImageDetectionTaskResultResponseBodyTamperBaseResultsPsLocItems] = None,
    ):
        # The PS tamper localization result description.
        self.desc = desc
        # The list of tampered regions.
        self.items = items

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
        if self.desc is not None:
            result['Desc'] = self.desc

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.GetImageDetectionTaskResultResponseBodyTamperBaseResultsPsLocItems()
                self.items.append(temp_model.from_map(k1))

        return self

class GetImageDetectionTaskResultResponseBodyTamperBaseResultsPsLocItems(DaraModel):
    def __init__(
        self,
        bbox: List[float] = None,
        score: float = None,
    ):
        # The bounding box coordinates of the tampered region, in the format `[x1, y1, x2, y2]`.
        self.bbox = bbox
        # The tamper confidence of the region. Value range: 0 to 1.
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bbox is not None:
            result['Bbox'] = self.bbox

        if self.score is not None:
            result['Score'] = self.score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        return self

class GetImageDetectionTaskResultResponseBodyTamperBaseResultsAips(DaraModel):
    def __init__(
        self,
        desc: str = None,
        risk: str = None,
        score: float = None,
    ):
        # The AI post-processing detection result description.
        self.desc = desc
        # The local PS/AI editing dimension risk label.
        self.risk = risk
        # The AI post-processing detection score. Value range: 0 to 1. A higher value indicates a greater likelihood of AI post-processing.
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.risk is not None:
            result['Risk'] = self.risk

        if self.score is not None:
            result['Score'] = self.score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Risk') is not None:
            self.risk = m.get('Risk')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        return self

class GetImageDetectionTaskResultResponseBodyTamperBaseResultsAigc(DaraModel):
    def __init__(
        self,
        desc: str = None,
        risk: str = None,
        score: float = None,
    ):
        # The AIGC detection result description.
        self.desc = desc
        # The AIGC dimension risk label.
        self.risk = risk
        # The AIGC detection score. Value range: 0 to 1. A higher value indicates a greater likelihood of AI generation.
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.risk is not None:
            result['Risk'] = self.risk

        if self.score is not None:
            result['Score'] = self.score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Risk') is not None:
            self.risk = m.get('Risk')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        return self

class GetImageDetectionTaskResultResponseBodyLabels(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        label: str = None,
    ):
        # The confidence level. Value range: 0 to 1.
        self.confidence = confidence
        # The detection label. When DetectMode is aigc, valid values are: risk_aigc (the image is suspected to be AIGC-generated), risk_fake (the image is suspected to be a composite image), risk_edit (the image is suspected to be AI-edited). When DetectMode is tamper, valid values are: aigc (AIGC detection score), aips (AI post-processing detection score).
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

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

