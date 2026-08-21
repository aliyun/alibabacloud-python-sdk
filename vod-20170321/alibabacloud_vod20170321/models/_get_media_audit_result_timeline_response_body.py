# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetMediaAuditResultTimelineResponseBody(DaraModel):
    def __init__(
        self,
        media_audit_result_timeline: main_models.GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimeline = None,
        request_id: str = None,
    ):
        # The collection of automated review result timelines.
        self.media_audit_result_timeline = media_audit_result_timeline
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.media_audit_result_timeline:
            self.media_audit_result_timeline.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_audit_result_timeline is not None:
            result['MediaAuditResultTimeline'] = self.media_audit_result_timeline.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaAuditResultTimeline') is not None:
            temp_model = main_models.GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimeline()
            self.media_audit_result_timeline = temp_model.from_map(m.get('MediaAuditResultTimeline'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimeline(DaraModel):
    def __init__(
        self,
        ad: List[main_models.GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineAd] = None,
        live: List[main_models.GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLive] = None,
        logo: List[main_models.GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLogo] = None,
        porn: List[main_models.GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelinePorn] = None,
        terrorism: List[main_models.GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineTerrorism] = None,
    ):
        # The collection of advertisement detection timelines.
        self.ad = ad
        # The collection of undesirable scene timelines.
        self.live = live
        # The collection of logo detection timelines.
        self.logo = logo
        # The collection of pornography detection timelines.
        self.porn = porn
        # The collection of terrorism detection timelines.
        self.terrorism = terrorism

    def validate(self):
        if self.ad:
            for v1 in self.ad:
                 if v1:
                    v1.validate()
        if self.live:
            for v1 in self.live:
                 if v1:
                    v1.validate()
        if self.logo:
            for v1 in self.logo:
                 if v1:
                    v1.validate()
        if self.porn:
            for v1 in self.porn:
                 if v1:
                    v1.validate()
        if self.terrorism:
            for v1 in self.terrorism:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ad'] = []
        if self.ad is not None:
            for k1 in self.ad:
                result['Ad'].append(k1.to_map() if k1 else None)

        result['Live'] = []
        if self.live is not None:
            for k1 in self.live:
                result['Live'].append(k1.to_map() if k1 else None)

        result['Logo'] = []
        if self.logo is not None:
            for k1 in self.logo:
                result['Logo'].append(k1.to_map() if k1 else None)

        result['Porn'] = []
        if self.porn is not None:
            for k1 in self.porn:
                result['Porn'].append(k1.to_map() if k1 else None)

        result['Terrorism'] = []
        if self.terrorism is not None:
            for k1 in self.terrorism:
                result['Terrorism'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ad = []
        if m.get('Ad') is not None:
            for k1 in m.get('Ad'):
                temp_model = main_models.GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineAd()
                self.ad.append(temp_model.from_map(k1))

        self.live = []
        if m.get('Live') is not None:
            for k1 in m.get('Live'):
                temp_model = main_models.GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLive()
                self.live.append(temp_model.from_map(k1))

        self.logo = []
        if m.get('Logo') is not None:
            for k1 in m.get('Logo'):
                temp_model = main_models.GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLogo()
                self.logo.append(temp_model.from_map(k1))

        self.porn = []
        if m.get('Porn') is not None:
            for k1 in m.get('Porn'):
                temp_model = main_models.GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelinePorn()
                self.porn.append(temp_model.from_map(k1))

        self.terrorism = []
        if m.get('Terrorism') is not None:
            for k1 in m.get('Terrorism'):
                temp_model = main_models.GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineTerrorism()
                self.terrorism.append(temp_model.from_map(k1))

        return self

class GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineTerrorism(DaraModel):
    def __init__(
        self,
        label: str = None,
        score: str = None,
        timestamp: str = None,
    ):
        # The terrorism and political content detection result. Valid values:
        # 
        # - **normal**: normal.
        # - **bloody**: bloody content.
        # - **explosion**: explosions and smoke.
        # - **outfit**: special attire.
        # - **logo**: special logos.
        # - **weapon**: weapons.
        # - **politics**: political content.
        # - **violence**: fighting.
        # - **crowd**: crowd gathering.
        # - **parade**: parades.
        # - **carcrash**: car accident scenes.
        # - **flag**: flags.
        # - **location**: landmarks.
        # - **others**: others.
        self.label = label
        # The hit score of the video screenshot for the terrorism and political content detection result. Value range: `[0-100]`, with a precision of 10 decimal places. The hit result indicates the probability of the corresponding classification label. A higher value indicates higher accuracy.
        self.score = score
        # The position in the video. Unit: milliseconds.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.score is not None:
            result['Score'] = self.score

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelinePorn(DaraModel):
    def __init__(
        self,
        label: str = None,
        score: str = None,
        timestamp: str = None,
    ):
        # The classification of the pornography detection result. Valid values:
        # 
        # - **porn**: pornographic content.
        # - **sexy**: sexually suggestive content.
        # - **normal**: normal content.
        self.label = label
        # The hit score of the video screenshot for the pornography detection result. Value range: `[0-100]`, with a precision of 10 decimal places. The hit result indicates the probability of the corresponding classification label. A higher value indicates higher accuracy.
        self.score = score
        # The position of the video screenshot in the video. Unit: milliseconds.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.score is not None:
            result['Score'] = self.score

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLogo(DaraModel):
    def __init__(
        self,
        label: str = None,
        score: str = None,
        timestamp: str = None,
    ):
        # The classification of the logo detection result. Valid values:
        # - **normal**: normal.
        # - **TV**: contains a regulated logo.
        # - **trademark**: contains a trademark.
        self.label = label
        # The hit score of the video screenshot for the logo detection result. Value range: `[0-100]`, with a precision of 10 decimal places. The hit result indicates the probability of the corresponding classification label. A higher value indicates higher accuracy.
        self.score = score
        # The position of the video screenshot in the video. Unit: milliseconds.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.score is not None:
            result['Score'] = self.score

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLive(DaraModel):
    def __init__(
        self,
        label: str = None,
        score: str = None,
        timestamp: str = None,
    ):
        # The classification of the undesirable content detection result. Valid values:
        # - **normal**: normal.
        # - **meaningless**: no content in the image (such as a black screen or white screen).
        # - **PIP**: Picture-in-Picture (PiP).
        # - **smoking**: smoking.
        # - **drivelive**: in-car live streaming.
        self.label = label
        # The hit score of the video screenshot for the undesirable content detection result. Value range: `[0-100]`, with a precision of 10 decimal places. The hit result indicates the probability of the corresponding classification label. A higher value indicates higher accuracy.
        self.score = score
        # The position of the video screenshot in the video. Unit: milliseconds.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.score is not None:
            result['Score'] = self.score

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineAd(DaraModel):
    def __init__(
        self,
        label: str = None,
        score: str = None,
        timestamp: str = None,
    ):
        # The classification of the advertisement detection result. Valid values:
        # - **normal**: normal.
        # - **ad**: other advertisements.
        # - **politics**: text contains political content.
        # - **porn**: text contains pornographic content.
        # - **abuse**: text contains abusive content.
        # - **terrorism**: text contains terrorism-related content.
        # - **contraband**: text contains prohibited content.
        # - **spam**: text contains other spam content.
        # - **npx**: psoriasis advertisements.
        # - **qrcode**: contains a QR code.
        # - **programCode**: contains a mini program code.
        self.label = label
        # The hit score of the video screenshot for the advertisement detection result. Value range: `[0-100]`, with a precision of 10 decimal places. The hit result indicates the probability of the corresponding classification label. A higher value indicates higher accuracy.
        self.score = score
        # The position of the video screenshot in the video. Unit: milliseconds.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.score is not None:
            result['Score'] = self.score

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

