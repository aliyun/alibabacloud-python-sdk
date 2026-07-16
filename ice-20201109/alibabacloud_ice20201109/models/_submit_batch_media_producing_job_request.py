# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitBatchMediaProducingJobRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        editing_config: str = None,
        input_config: str = None,
        output_config: str = None,
        template_config: str = None,
        user_data: str = None,
    ):
        # A client-side token used to ensure request idempotence.
        self.client_token = client_token
        # The editing configuration. For the structure definition, see [EditingConfig](~~2692547#1be9bba03b7qu~~).
        self.editing_config = editing_config
        # The input configuration. For the structure definition, see [InputConfig](~~2692547#2faed1559549n~~).
        self.input_config = input_config
        # The output configuration. For the structure definition, see [OutputConfig](~~2692547#447b928fcbuoa~~).
        self.output_config = output_config
        # The template parameters. You can configure multiple templates for one-click smart video creation. The system randomly selects one template to apply. For more information, see [TemplateConfig parameters](https://help.aliyun.com/zh/ims/use-cases/batch-video-production-public-parameters?spm=a2c4g.11186623.help-menu-193643.d_3_2_0_5.342860c5H30VVS\\&scm=20140722.H_2877814._.OR_help-T_cn~zh-V_1#32c3bea6182sy).
        self.template_config = template_config
        # Custom business and callback configurations. For the structure definition, see [UserData configuration](~~357745#section-urj-v3f-0s1~~).
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config

        if self.input_config is not None:
            result['InputConfig'] = self.input_config

        if self.output_config is not None:
            result['OutputConfig'] = self.output_config

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')

        if m.get('InputConfig') is not None:
            self.input_config = m.get('InputConfig')

        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')

        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

