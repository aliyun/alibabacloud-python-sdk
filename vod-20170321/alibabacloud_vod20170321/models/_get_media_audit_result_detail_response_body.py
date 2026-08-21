# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetMediaAuditResultDetailResponseBody(DaraModel):
    def __init__(
        self,
        media_audit_result_detail: main_models.GetMediaAuditResultDetailResponseBodyMediaAuditResultDetail = None,
        request_id: str = None,
    ):
        # The details of the review results.
        self.media_audit_result_detail = media_audit_result_detail
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.media_audit_result_detail:
            self.media_audit_result_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_audit_result_detail is not None:
            result['MediaAuditResultDetail'] = self.media_audit_result_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaAuditResultDetail') is not None:
            temp_model = main_models.GetMediaAuditResultDetailResponseBodyMediaAuditResultDetail()
            self.media_audit_result_detail = temp_model.from_map(m.get('MediaAuditResultDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMediaAuditResultDetailResponseBodyMediaAuditResultDetail(DaraModel):
    def __init__(
        self,
        list: List[main_models.GetMediaAuditResultDetailResponseBodyMediaAuditResultDetailList] = None,
        total: int = None,
    ):
        # The list of video review result details.
        self.list = list
        # The total number of video review result screenshots.
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.GetMediaAuditResultDetailResponseBodyMediaAuditResultDetailList()
                self.list.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetMediaAuditResultDetailResponseBodyMediaAuditResultDetailList(DaraModel):
    def __init__(
        self,
        ad_label: str = None,
        ad_score: str = None,
        live_label: str = None,
        live_score: str = None,
        logo_label: str = None,
        logo_score: str = None,
        porn_label: str = None,
        porn_score: str = None,
        terrorism_label: str = None,
        terrorism_score: str = None,
        timestamp: str = None,
        url: str = None,
    ):
        # The classification of the ad review result. Valid values:
        # - **normal**: Normal.
        # - **ad**: Other ads.
        # - **politics**: Text contains politically sensitive content.
        # - **porn**: Text contains pornographic content.
        # - **abuse**: Text contains abusive content.
        # - **terrorism**: Text contains terrorism-related content.
        # - **contraband**: Text contains prohibited content.
        # - **spam**: Text contains other spam content.
        # - **npx**: Psoriasis ads.
        # - **qrcode**: Contains a QR code.
        # - **programCode**: Contains a mini program code.
        self.ad_label = ad_label
        # The hit score of the video screenshot for the ad review result. Value range: `[0-100]`, with a precision of 10 decimal places. The hit result indicates the probability of the corresponding classification label. A higher value indicates higher accuracy.
        self.ad_score = ad_score
        # The classification of the undesirable scene review result. Valid values:
        # - **normal**: Normal.
        # - **meaningless**: The image has no content (for example, a black screen or white screen).
        # - **PIP**: Picture-in-Picture (PiP).
        # - **smoking**: Smoking.
        # - **drivelive**: In-car live streaming.
        self.live_label = live_label
        # The hit score of the video screenshot for the undesirable scene review result. Value range: `[0-100]`, with a precision of 10 decimal places. The hit result indicates the probability of the corresponding classification label. A higher value indicates higher accuracy.
        self.live_score = live_score
        # The classification of the logo review result. Valid values:
        # - **normal**: Normal.
        # - **TV**: Contains a regulated logo.
        # - **trademark**: Contains a trademark.
        self.logo_label = logo_label
        # The hit score of the video screenshot for the logo review result. Value range: `[0-100]`, with a precision of 10 decimal places. The hit result indicates the probability of the corresponding classification label. A higher value indicates higher accuracy.
        self.logo_score = logo_score
        # The classification of the pornography review result. Valid values:
        # 
        # - **normal**: Normal.
        # - **porn**: Pornographic.
        # - **sexy**: Sexy.
        self.porn_label = porn_label
        # The hit score of the video screenshot for the pornography review result. Value range: `[0-100]`, with a precision of 10 decimal places. The hit result indicates the probability of the corresponding classification label. A higher value indicates higher accuracy.
        self.porn_score = porn_score
        # The classification of the terrorism review result. Valid values:
        # 
        # - **normal**: Normal.
        # - **bloody**: Bloody.
        # - **explosion**: Explosion and smoke.
        # - **outfit**: Special attire.
        # - **logo**: Special logo.
        # - **weapon**: Weapon.
        # - **politics**: Politically sensitive.
        # - **violence**: Fighting.
        # - **crowd**: Crowd gathering.
        # - **parade**: Parade.
        # - **carcrash**: Car crash scene.
        # - **flag**: Flag.
        # - **location**: Landmark.
        # - **others**: Others.
        self.terrorism_label = terrorism_label
        # The hit score of the video screenshot for the terrorism review result. Value range: `[0-100]`, with a precision of 10 decimal places. The hit result indicates the probability of the corresponding classification label. A higher value indicates higher accuracy.
        self.terrorism_score = terrorism_score
        # The position of the video screenshot in the video. Unit: milliseconds.
        self.timestamp = timestamp
        # The URL of the video screenshot.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_label is not None:
            result['AdLabel'] = self.ad_label

        if self.ad_score is not None:
            result['AdScore'] = self.ad_score

        if self.live_label is not None:
            result['LiveLabel'] = self.live_label

        if self.live_score is not None:
            result['LiveScore'] = self.live_score

        if self.logo_label is not None:
            result['LogoLabel'] = self.logo_label

        if self.logo_score is not None:
            result['LogoScore'] = self.logo_score

        if self.porn_label is not None:
            result['PornLabel'] = self.porn_label

        if self.porn_score is not None:
            result['PornScore'] = self.porn_score

        if self.terrorism_label is not None:
            result['TerrorismLabel'] = self.terrorism_label

        if self.terrorism_score is not None:
            result['TerrorismScore'] = self.terrorism_score

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdLabel') is not None:
            self.ad_label = m.get('AdLabel')

        if m.get('AdScore') is not None:
            self.ad_score = m.get('AdScore')

        if m.get('LiveLabel') is not None:
            self.live_label = m.get('LiveLabel')

        if m.get('LiveScore') is not None:
            self.live_score = m.get('LiveScore')

        if m.get('LogoLabel') is not None:
            self.logo_label = m.get('LogoLabel')

        if m.get('LogoScore') is not None:
            self.logo_score = m.get('LogoScore')

        if m.get('PornLabel') is not None:
            self.porn_label = m.get('PornLabel')

        if m.get('PornScore') is not None:
            self.porn_score = m.get('PornScore')

        if m.get('TerrorismLabel') is not None:
            self.terrorism_label = m.get('TerrorismLabel')

        if m.get('TerrorismScore') is not None:
            self.terrorism_score = m.get('TerrorismScore')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

