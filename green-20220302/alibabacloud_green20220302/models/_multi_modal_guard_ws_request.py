# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MultiModalGuardWsRequest(DaraModel):
    def __init__(
        self,
        model_type: str = None,
        protocol_type: str = None,
        service: str = None,
        service_parameters: str = None,
    ):
        # The model type. Valid values:
        # 
        # - LLM
        self.model_type = model_type
        # The protocol type. Valid values:
        # 
        # - OpenAI
        # - DashScope
        # - Anthropic
        self.protocol_type = protocol_type
        # The moderation service category. Valid values:
        # 
        # - query_security_check_pro: AI input content security detection (pro edition).
        # - response_security_check_pro: AI-generated content security detection (pro edition).
        # - img_query_security_check: AIGC input image security detection.
        # - img_response_security_check: AIGC output image security detection.
        # - text_img_mix_guard: Multimodal (text + image) hybrid security detection.
        # - file_security_sync_check: AIGC input or output file security detection.
        # - text_file_sec_sync_check: Multimodal (text + file) real-time security detection.
        self.service = service
        # The parameter set required by the moderation service, in JSON string format. The input parameter for text content is content (String), the input parameter for image content is imageUrls (JSONArray), and the input parameter for file content is fileUrls (JSONArray).
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.service is not None:
            result['Service'] = self.service

        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')

        return self

