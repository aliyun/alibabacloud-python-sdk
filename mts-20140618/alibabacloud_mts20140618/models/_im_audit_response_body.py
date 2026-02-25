# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class ImAuditResponseBody(DaraModel):
    def __init__(
        self,
        image_quota_exceed: bool = None,
        image_results: main_models.ImAuditResponseBodyImageResults = None,
        request_id: str = None,
        text_quota_exceed: bool = None,
        text_results: main_models.ImAuditResponseBodyTextResults = None,
    ):
        # Indicates whether the image moderation QPS exceeds the limit. Valid values: true and false. A value of true indicates that the QPS does not exceed the limit. A value of false indicates that the QPS exceeds the limit.
        self.image_quota_exceed = image_quota_exceed
        # The image moderation results. If the HTTP status code 200 is returned, the array in the returned results contains one or more elements. For more information about the parameters, see [Data returned by the ImAudit operation](https://help.aliyun.com/document_detail/268644.html).
        self.image_results = image_results
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the text moderation QPS exceeds the limit. Valid values: true and false.
        self.text_quota_exceed = text_quota_exceed
        # The text moderation results. If the HTTP status code 200 is returned, the array in the returned results contains one or more elements. For more information about the parameters, see [Data returned by the ImAudit operation](https://help.aliyun.com/document_detail/268644.html).
        self.text_results = text_results

    def validate(self):
        if self.image_results:
            self.image_results.validate()
        if self.text_results:
            self.text_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_quota_exceed is not None:
            result['ImageQuotaExceed'] = self.image_quota_exceed

        if self.image_results is not None:
            result['ImageResults'] = self.image_results.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.text_quota_exceed is not None:
            result['TextQuotaExceed'] = self.text_quota_exceed

        if self.text_results is not None:
            result['TextResults'] = self.text_results.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageQuotaExceed') is not None:
            self.image_quota_exceed = m.get('ImageQuotaExceed')

        if m.get('ImageResults') is not None:
            temp_model = main_models.ImAuditResponseBodyImageResults()
            self.image_results = temp_model.from_map(m.get('ImageResults'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TextQuotaExceed') is not None:
            self.text_quota_exceed = m.get('TextQuotaExceed')

        if m.get('TextResults') is not None:
            temp_model = main_models.ImAuditResponseBodyTextResults()
            self.text_results = temp_model.from_map(m.get('TextResults'))

        return self

class ImAuditResponseBodyTextResults(DaraModel):
    def __init__(
        self,
        result: List[main_models.ImAuditResponseBodyTextResultsResult] = None,
    ):
        # The text moderation results.
        self.result = result

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
        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ImAuditResponseBodyTextResultsResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ImAuditResponseBodyTextResultsResult(DaraModel):
    def __init__(
        self,
        code: int = None,
        content: str = None,
        data_id: str = None,
        msg: str = None,
        results: List[main_models.ImAuditResponseBodyTextResultsResultResults] = None,
        task_id: str = None,
    ):
        # The error code. The error code is the same as the HTTP status code. For more information, see [Error codes](https://help.aliyun.com/document_detail/29254.html).
        self.code = code
        # The text that you specify in the moderation request.
        self.content = content
        # The sequence number of the text.
        self.data_id = data_id
        # The message that is returned for the request.
        self.msg = msg
        # The returned data. If the HTTP status code 200 is returned, the array in the returned results contains one or more elements. Each element is a struct.
        self.results = results
        # The ID of the moderation task.
        self.task_id = task_id

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.content is not None:
            result['content'] = self.content

        if self.data_id is not None:
            result['dataId'] = self.data_id

        if self.msg is not None:
            result['msg'] = self.msg

        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')

        if m.get('msg') is not None:
            self.msg = m.get('msg')

        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.ImAuditResponseBodyTextResultsResultResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

class ImAuditResponseBodyTextResultsResultResults(DaraModel):
    def __init__(
        self,
        details: List[main_models.ImAuditResponseBodyTextResultsResultResultsDetails] = None,
        label: str = None,
        rate: float = None,
        scene: str = None,
        suggestion: str = None,
    ):
        # The risky content that the moderated text hits. A text entry can hit multiple pieces of risky content.
        self.details = details
        # The category of the moderation result for the moderated text. Valid values:
        # 
        # *   normal: normal content
        # *   spam: spam
        # *   ad: ad
        # *   politics: political content
        # *   terrorism: terrorist content
        # *   abuse: abuse
        # *   porn: pornographic content
        # *   flood: excessive junk content
        # *   contraband: prohibited content
        # *   meaningless: meaningless content
        # *   customized: custom content, such as a custom keyword
        self.label = label
        # The score of the confidence level. Valid values: 0 to 100. A greater value indicates a higher confidence level. If a value of pass is returned for the suggestion parameter, a higher confidence level indicates a higher probability that the content is normal. If a value of review or block is returned for the suggestion parameter, a higher confidence level indicates a higher probability that the content contains violations.
        # 
        # >  This score is for reference only. We strongly recommend that you do not use this score in your business. We recommend that you use the values that are returned for the suggestion, label, and sublabel parameters to determine whether the content contains violations. The sublabel parameter is returned by some operations.
        self.rate = rate
        # The moderation scenario.
        self.scene = scene
        # The recommended subsequent operation. Valid values:
        # 
        # *   pass: The content passes the moderation.
        # *   review: The content needs to be manually reviewed again.
        # *   block: The content contains violations. We recommend that you delete or block the content.
        self.suggestion = suggestion

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['details'].append(k1.to_map() if k1 else None)

        if self.label is not None:
            result['label'] = self.label

        if self.rate is not None:
            result['rate'] = self.rate

        if self.scene is not None:
            result['scene'] = self.scene

        if self.suggestion is not None:
            result['suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.details = []
        if m.get('details') is not None:
            for k1 in m.get('details'):
                temp_model = main_models.ImAuditResponseBodyTextResultsResultResultsDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('rate') is not None:
            self.rate = m.get('rate')

        if m.get('scene') is not None:
            self.scene = m.get('scene')

        if m.get('suggestion') is not None:
            self.suggestion = m.get('suggestion')

        return self

class ImAuditResponseBodyTextResultsResultResultsDetails(DaraModel):
    def __init__(
        self,
        label: str = None,
        contexts: List[main_models.ImAuditResponseBodyTextResultsResultResultsDetailsContexts] = None,
    ):
        # The category of the risky content that the moderated text hits. Valid values:
        # 
        # *   spam: spam
        # *   ad: ad
        # *   politics: political content
        # *   terrorism: terrorist content
        # *   abuse: abuse
        # *   porn: pornographic content
        # *   flood: excessive junk content
        # *   contraband: prohibited content
        # *   meaningless: meaningless content
        # *   customized: custom content, such as a custom keyword
        self.label = label
        # The context information of the risky content that the moderated text hits.
        self.contexts = contexts

    def validate(self):
        if self.contexts:
            for v1 in self.contexts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        result['contexts'] = []
        if self.contexts is not None:
            for k1 in self.contexts:
                result['contexts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        self.contexts = []
        if m.get('contexts') is not None:
            for k1 in m.get('contexts'):
                temp_model = main_models.ImAuditResponseBodyTextResultsResultResultsDetailsContexts()
                self.contexts.append(temp_model.from_map(k1))

        return self

class ImAuditResponseBodyTextResultsResultResultsDetailsContexts(DaraModel):
    def __init__(
        self,
        context: str = None,
        lib_code: str = None,
        lib_name: str = None,
        positions: List[str] = None,
        rule_type: str = None,
    ):
        # The term that the moderated text hits. If the text hits a term, the term is returned. If the text hits the algorithmic model, this parameter is not returned.
        self.context = context
        # The code of the custom text library. This parameter is returned if the moderated text hits a term in the custom text library.
        self.lib_code = lib_code
        # The name of the custom text library. This parameter is returned if the moderated text hits a term in the custom text library.
        self.lib_name = lib_name
        # The position of the term that the moderated text hits in the original text.
        self.positions = positions
        # The behavior rule. This parameter is returned if the moderated text hits the behavior rule. Valid values:
        # 
        # *   user_id
        # *   ip
        # *   umid
        # *   content
        # *   similar_content
        # *   imei
        # *   imsi
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context is not None:
            result['context'] = self.context

        if self.lib_code is not None:
            result['libCode'] = self.lib_code

        if self.lib_name is not None:
            result['libName'] = self.lib_name

        if self.positions is not None:
            result['positions'] = self.positions

        if self.rule_type is not None:
            result['ruleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('context') is not None:
            self.context = m.get('context')

        if m.get('libCode') is not None:
            self.lib_code = m.get('libCode')

        if m.get('libName') is not None:
            self.lib_name = m.get('libName')

        if m.get('positions') is not None:
            self.positions = m.get('positions')

        if m.get('ruleType') is not None:
            self.rule_type = m.get('ruleType')

        return self

class ImAuditResponseBodyImageResults(DaraModel):
    def __init__(
        self,
        result: List[main_models.ImAuditResponseBodyImageResultsResult] = None,
    ):
        # The image moderation results.
        self.result = result

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
        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ImAuditResponseBodyImageResultsResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ImAuditResponseBodyImageResultsResult(DaraModel):
    def __init__(
        self,
        code: int = None,
        data_id: str = None,
        extras: Dict[str, Any] = None,
        msg: str = None,
        results: List[main_models.ImAuditResponseBodyImageResultsResultResults] = None,
        task_id: str = None,
        url: str = None,
    ):
        # The error code. The error code is the same as the HTTP status code. This parameter is not returned if the request is successful.
        self.code = code
        # The ID of the moderated object.
        # 
        # >  If you set the dataId parameter in the moderation request, the dataId parameter is returned in the response.
        self.data_id = data_id
        # The additional information about the image. If ad is specified for the Scenes parameter, the following content may be returned for this parameter: hitLibInfo: the information about the custom text library that is hit by the text in the image. The value of this parameter is an array. For more information about the structure, see [hitLibInfo](https://help.aliyun.com/document_detail/268644.html).
        self.extras = extras
        # The message that is returned for the request.
        self.msg = msg
        # The returned data. If the call is successful, the array in the returned results contains one or more elements. Each element is a struct.
        self.results = results
        # The ID of the moderation task.
        self.task_id = task_id
        # The URL of the moderated object.
        self.url = url

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data_id is not None:
            result['dataId'] = self.data_id

        if self.extras is not None:
            result['extras'] = self.extras

        if self.msg is not None:
            result['msg'] = self.msg

        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')

        if m.get('extras') is not None:
            self.extras = m.get('extras')

        if m.get('msg') is not None:
            self.msg = m.get('msg')

        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.ImAuditResponseBodyImageResultsResultResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ImAuditResponseBodyImageResultsResultResults(DaraModel):
    def __init__(
        self,
        label: str = None,
        rate: float = None,
        scene: str = None,
        suggestion: str = None,
        frames: List[main_models.ImAuditResponseBodyImageResultsResultResultsFrames] = None,
        hint_words_info: List[main_models.ImAuditResponseBodyImageResultsResultResultsHintWordsInfo] = None,
        logo_data: List[main_models.ImAuditResponseBodyImageResultsResultResultsLogoData] = None,
        ocr_data: List[str] = None,
        program_code_data: List[main_models.ImAuditResponseBodyImageResultsResultResultsProgramCodeData] = None,
        qrcode_data: List[str] = None,
        qrcode_locations: List[main_models.ImAuditResponseBodyImageResultsResultResultsQrcodeLocations] = None,
        sface_data: List[main_models.ImAuditResponseBodyImageResultsResultResultsSfaceData] = None,
    ):
        # The category of the moderation results. Valid values vary based on the specified moderation scenario.
        # 
        # *   If the Scenes parameter is set to porn, the valid values are:
        # 
        #     *   normal: no pornographic content
        #     *   sexy: sexy content
        #     *   porn: pornographic content
        # 
        # *   If the Scenes parameter is set to terrorism, the valid values are:
        # 
        #     *   normal: no pornographic content
        #     *   bloody: bloody content
        #     *   explosion: explosions and smoke
        #     *   outfit: special costume
        #     *   logo: special logo
        #     *   weapon: weapon
        #     *   politics: political content
        #     *   violence: violence
        #     *   crowd: crowd
        #     *   parade: parade
        #     *   carcrash: car accident
        #     *   flag: flag
        #     *   location: landmark
        #     *   others: other content
        # 
        # *   If the Scenes parameter is set to ad, the valid values are:
        # 
        #     *   normal: no pornographic content
        #     *   ad: ad violation
        #     *   politics: politically sensitive content in text
        #     *   porn: pornographic content in text
        #     *   abuse: abuse in text
        #     *   terrorism: terrorist content in text
        #     *   contraband: prohibited content in text
        #     *   spam: junk content in text
        #     *   npx: illegal ad
        #     *   qrcode: QR code
        #     *   programCode: mini program code
        # 
        # *   If the Scenes parameter is set to qrcode, the valid values are:
        # 
        #     *   normal: no pornographic content
        #     *   qrcode: QR code
        #     *   programCode: mini program code
        # 
        # *   If the Scenes parameter is set to live, the valid values are:
        # 
        #     *   normal: no pornographic content
        #     *   meaningless: no content in the image, such as black or white screen
        #     *   PIP: picture-in-picture
        #     *   smoking: smoking
        #     *   drivelive: live broadcasting in a running vehicle
        # 
        # *   If the Scenes parameter is set to logo, the valid values are:
        # 
        #     *   normal: no pornographic content
        #     *   TV: controlled logo
        #     *   trademark: trademark
        self.label = label
        # The score of the confidence level. Valid values: 0 to 100. A greater value indicates a higher confidence level. If a value of pass is returned for the suggestion parameter, a higher confidence level indicates a higher probability that the content is normal. If a value of review or block is returned for the suggestion parameter, a higher confidence level indicates a higher probability that the content contains violations.
        # 
        # >  This score is for reference only. We strongly recommend that you do not use this score in your business. We recommend that you use the values that are returned for the suggestion, label, and sublabel parameters to determine whether the content contains violations. The sublabel parameter is returned by some operations.
        self.rate = rate
        # The image moderation scenario. Valid values:
        # 
        # *   porn: pornography
        # *   terrorism: terrorist content
        # *   ad: ad violation
        # *   qrcode: QR code
        # *   live: undesirable scene
        # *   logo: special logo
        self.scene = scene
        # The recommended subsequent operation. Valid values:
        # 
        # *   pass: The content passes the moderation. No further actions are required.
        # *   review: The moderation object contains suspected violations and requires human review.
        # *   block: The moderation object contains violations. We recommend that you delete or block the object.
        self.suggestion = suggestion
        # If the temporary access URL of the image is too long, a truncated temporary access URL is returned for each frame.
        self.frames = frames
        # The information about the term hit by the ad or violation text detected in the moderated image.
        self.hint_words_info = hint_words_info
        # The information about the logo detected in the moderated image.
        self.logo_data = logo_data
        # ocrData
        self.ocr_data = ocr_data
        # The location information of the mini program code detected in the moderated image.
        self.program_code_data = program_code_data
        # The information about the text that is included in the QR code detected in the moderated image.
        self.qrcode_data = qrcode_data
        # The coordinates of the QR code detected in the image.
        self.qrcode_locations = qrcode_locations
        # The information about the terrorist content detected in the moderated image.
        self.sface_data = sface_data

    def validate(self):
        if self.frames:
            for v1 in self.frames:
                 if v1:
                    v1.validate()
        if self.hint_words_info:
            for v1 in self.hint_words_info:
                 if v1:
                    v1.validate()
        if self.logo_data:
            for v1 in self.logo_data:
                 if v1:
                    v1.validate()
        if self.program_code_data:
            for v1 in self.program_code_data:
                 if v1:
                    v1.validate()
        if self.qrcode_locations:
            for v1 in self.qrcode_locations:
                 if v1:
                    v1.validate()
        if self.sface_data:
            for v1 in self.sface_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.rate is not None:
            result['Rate'] = self.rate

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        result['frames'] = []
        if self.frames is not None:
            for k1 in self.frames:
                result['frames'].append(k1.to_map() if k1 else None)

        result['hintWordsInfo'] = []
        if self.hint_words_info is not None:
            for k1 in self.hint_words_info:
                result['hintWordsInfo'].append(k1.to_map() if k1 else None)

        result['logoData'] = []
        if self.logo_data is not None:
            for k1 in self.logo_data:
                result['logoData'].append(k1.to_map() if k1 else None)

        if self.ocr_data is not None:
            result['ocrData'] = self.ocr_data

        result['programCodeData'] = []
        if self.program_code_data is not None:
            for k1 in self.program_code_data:
                result['programCodeData'].append(k1.to_map() if k1 else None)

        if self.qrcode_data is not None:
            result['qrcodeData'] = self.qrcode_data

        result['qrcodeLocations'] = []
        if self.qrcode_locations is not None:
            for k1 in self.qrcode_locations:
                result['qrcodeLocations'].append(k1.to_map() if k1 else None)

        result['sfaceData'] = []
        if self.sface_data is not None:
            for k1 in self.sface_data:
                result['sfaceData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        self.frames = []
        if m.get('frames') is not None:
            for k1 in m.get('frames'):
                temp_model = main_models.ImAuditResponseBodyImageResultsResultResultsFrames()
                self.frames.append(temp_model.from_map(k1))

        self.hint_words_info = []
        if m.get('hintWordsInfo') is not None:
            for k1 in m.get('hintWordsInfo'):
                temp_model = main_models.ImAuditResponseBodyImageResultsResultResultsHintWordsInfo()
                self.hint_words_info.append(temp_model.from_map(k1))

        self.logo_data = []
        if m.get('logoData') is not None:
            for k1 in m.get('logoData'):
                temp_model = main_models.ImAuditResponseBodyImageResultsResultResultsLogoData()
                self.logo_data.append(temp_model.from_map(k1))

        if m.get('ocrData') is not None:
            self.ocr_data = m.get('ocrData')

        self.program_code_data = []
        if m.get('programCodeData') is not None:
            for k1 in m.get('programCodeData'):
                temp_model = main_models.ImAuditResponseBodyImageResultsResultResultsProgramCodeData()
                self.program_code_data.append(temp_model.from_map(k1))

        if m.get('qrcodeData') is not None:
            self.qrcode_data = m.get('qrcodeData')

        self.qrcode_locations = []
        if m.get('qrcodeLocations') is not None:
            for k1 in m.get('qrcodeLocations'):
                temp_model = main_models.ImAuditResponseBodyImageResultsResultResultsQrcodeLocations()
                self.qrcode_locations.append(temp_model.from_map(k1))

        self.sface_data = []
        if m.get('sfaceData') is not None:
            for k1 in m.get('sfaceData'):
                temp_model = main_models.ImAuditResponseBodyImageResultsResultResultsSfaceData()
                self.sface_data.append(temp_model.from_map(k1))

        return self

class ImAuditResponseBodyImageResultsResultResultsSfaceData(DaraModel):
    def __init__(
        self,
        faces: List[main_models.ImAuditResponseBodyImageResultsResultResultsSfaceDataFaces] = None,
        h: float = None,
        w: float = None,
        x: float = None,
        y: float = None,
    ):
        # The information about the face detected in the moderated image.
        self.faces = faces
        # The height of the face area. Unit: pixel.
        self.h = h
        # The width of the face area. Unit: pixel.
        self.w = w
        # The distance between the upper-left corner of the face area and the y-axis, with the upper-left corner of the image being the coordinate origin. Unit: pixel.
        self.x = x
        # The distance between the upper-left corner of the face area and the y-axis, with the upper-left corner of the image being the coordinate origin. Unit: pixel.
        self.y = y

    def validate(self):
        if self.faces:
            for v1 in self.faces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['faces'] = []
        if self.faces is not None:
            for k1 in self.faces:
                result['faces'].append(k1.to_map() if k1 else None)

        if self.h is not None:
            result['h'] = self.h

        if self.w is not None:
            result['w'] = self.w

        if self.x is not None:
            result['x'] = self.x

        if self.y is not None:
            result['y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.faces = []
        if m.get('faces') is not None:
            for k1 in m.get('faces'):
                temp_model = main_models.ImAuditResponseBodyImageResultsResultResultsSfaceDataFaces()
                self.faces.append(temp_model.from_map(k1))

        if m.get('h') is not None:
            self.h = m.get('h')

        if m.get('w') is not None:
            self.w = m.get('w')

        if m.get('x') is not None:
            self.x = m.get('x')

        if m.get('y') is not None:
            self.y = m.get('y')

        return self

class ImAuditResponseBodyImageResultsResultResultsSfaceDataFaces(DaraModel):
    def __init__(
        self,
        idid: str = None,
        name: str = None,
        re: float = None,
    ):
        # The ID of the detected face. The value is a string.
        self.idid = idid
        # This value is a string, which indicates the name of a similar person.
        self.name = name
        # The score of the confidence level. The value is a float point number. Valid values: 0 to 100. A greater value indicates a higher confidence level for facial recognition.
        self.re = re

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.idid is not None:
            result['idid'] = self.idid

        if self.name is not None:
            result['name'] = self.name

        if self.re is not None:
            result['re'] = self.re

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('idid') is not None:
            self.idid = m.get('idid')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('re') is not None:
            self.re = m.get('re')

        return self

class ImAuditResponseBodyImageResultsResultResultsQrcodeLocations(DaraModel):
    def __init__(
        self,
        h: float = None,
        qrcode: str = None,
        w: float = None,
        x: float = None,
        y: float = None,
    ):
        # The height of the QR code area. Unit: pixel.
        self.h = h
        # The URL that the detected QR code points to.
        self.qrcode = qrcode
        # The width of the QR code area. Unit: pixel.
        self.w = w
        # The distance between the upper-left corner of the QR code area and the y-axis, with the upper-left corner of the image being the coordinate origin. Unit: pixel.
        self.x = x
        # The distance between the upper-left corner of the QR code area and the x-axis, with the upper-left corner of the image being the coordinate origin. Unit: pixel.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.h is not None:
            result['h'] = self.h

        if self.qrcode is not None:
            result['qrcode'] = self.qrcode

        if self.w is not None:
            result['w'] = self.w

        if self.x is not None:
            result['x'] = self.x

        if self.y is not None:
            result['y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('h') is not None:
            self.h = m.get('h')

        if m.get('qrcode') is not None:
            self.qrcode = m.get('qrcode')

        if m.get('w') is not None:
            self.w = m.get('w')

        if m.get('x') is not None:
            self.x = m.get('x')

        if m.get('y') is not None:
            self.y = m.get('y')

        return self

class ImAuditResponseBodyImageResultsResultResultsProgramCodeData(DaraModel):
    def __init__(
        self,
        h: float = None,
        w: float = None,
        x: float = None,
        y: float = None,
    ):
        # The height of the mini program code area. Unit: pixel.
        self.h = h
        # The width of the mini program code area. Unit: pixel.
        self.w = w
        # The distance between the upper-left corner of the mini program code area and the y-axis, with the upper-left corner of the image being the coordinate origin. Unit: pixel.
        self.x = x
        # The distance between the upper-left corner of the mini program code area and the x-axis, with the upper-left corner of the image being the coordinate origin. Unit: pixel.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.h is not None:
            result['h'] = self.h

        if self.w is not None:
            result['w'] = self.w

        if self.x is not None:
            result['x'] = self.x

        if self.y is not None:
            result['y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('h') is not None:
            self.h = m.get('h')

        if m.get('w') is not None:
            self.w = m.get('w')

        if m.get('x') is not None:
            self.x = m.get('x')

        if m.get('y') is not None:
            self.y = m.get('y')

        return self

class ImAuditResponseBodyImageResultsResultResultsLogoData(DaraModel):
    def __init__(
        self,
        h: float = None,
        name: str = None,
        type: str = None,
        w: float = None,
        x: float = None,
        y: float = None,
    ):
        # The height of the logo area. Unit: pixel.
        self.h = h
        # The name of the detected logo.
        self.name = name
        # The type of the detected logo. For example, a value of TV indicates a controlled media logo.
        self.type = type
        # The width of the logo area. Unit: pixel.
        self.w = w
        # The distance between the upper-left corner of the logo area and the y-axis, with the upper-left corner of the image being the coordinate origin. Unit: pixel.
        self.x = x
        # The distance between the upper-left corner of the logo area and the x-axis, with the upper-left corner of the image being the coordinate origin. Unit: pixel.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.h is not None:
            result['h'] = self.h

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.w is not None:
            result['w'] = self.w

        if self.x is not None:
            result['x'] = self.x

        if self.y is not None:
            result['y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('h') is not None:
            self.h = m.get('h')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('w') is not None:
            self.w = m.get('w')

        if m.get('x') is not None:
            self.x = m.get('x')

        if m.get('y') is not None:
            self.y = m.get('y')

        return self

class ImAuditResponseBodyImageResultsResultResultsHintWordsInfo(DaraModel):
    def __init__(
        self,
        context: str = None,
    ):
        # The term hit by the detected text.
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context is not None:
            result['context'] = self.context

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('context') is not None:
            self.context = m.get('context')

        return self

class ImAuditResponseBodyImageResultsResultResultsFrames(DaraModel):
    def __init__(
        self,
        rate: float = None,
        url: str = None,
    ):
        # The score of the confidence level. Valid values: 0 to 100. A higher confidence level indicates higher reliability of the moderation result. We recommend that you do not use this score in your business.
        self.rate = rate
        # The temporary access URL of the truncated frame. The URL is valid for 5 minutes.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rate is not None:
            result['rate'] = self.rate

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rate') is not None:
            self.rate = m.get('rate')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

