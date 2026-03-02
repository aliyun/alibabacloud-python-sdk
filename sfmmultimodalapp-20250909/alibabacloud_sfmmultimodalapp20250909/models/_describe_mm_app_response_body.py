# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sfmmultimodalapp20250909 import models as main_models
from darabonba.model import DaraModel

class DescribeMmAppResponseBody(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        conversation_config: main_models.DescribeMmAppResponseBodyConversationConfig = None,
        create_user_id: str = None,
        create_user_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        model_config: main_models.DescribeMmAppResponseBodyModelConfig = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        prompt: str = None,
        publish_version: int = None,
        request_id: str = None,
        status: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.conversation_config = conversation_config
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.model_config = model_config
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.prompt = prompt
        self.publish_version = publish_version
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.conversation_config:
            self.conversation_config.validate()
        if self.model_config:
            self.model_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.conversation_config is not None:
            result['ConversationConfig'] = self.conversation_config.to_map()

        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.model_config is not None:
            result['ModelConfig'] = self.model_config.to_map()

        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id

        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.publish_version is not None:
            result['PublishVersion'] = self.publish_version

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ConversationConfig') is not None:
            temp_model = main_models.DescribeMmAppResponseBodyConversationConfig()
            self.conversation_config = temp_model.from_map(m.get('ConversationConfig'))

        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ModelConfig') is not None:
            temp_model = main_models.DescribeMmAppResponseBodyModelConfig()
            self.model_config = temp_model.from_map(m.get('ModelConfig'))

        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')

        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('PublishVersion') is not None:
            self.publish_version = m.get('PublishVersion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeMmAppResponseBodyModelConfig(DaraModel):
    def __init__(
        self,
        history_limit: int = None,
        model_type: str = None,
        open_web_search: bool = None,
        text_modal: str = None,
    ):
        self.history_limit = history_limit
        self.model_type = model_type
        self.open_web_search = open_web_search
        self.text_modal = text_modal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.history_limit is not None:
            result['HistoryLimit'] = self.history_limit

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.open_web_search is not None:
            result['OpenWebSearch'] = self.open_web_search

        if self.text_modal is not None:
            result['TextModal'] = self.text_modal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HistoryLimit') is not None:
            self.history_limit = m.get('HistoryLimit')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('OpenWebSearch') is not None:
            self.open_web_search = m.get('OpenWebSearch')

        if m.get('TextModal') is not None:
            self.text_modal = m.get('TextModal')

        return self

class DescribeMmAppResponseBodyConversationConfig(DaraModel):
    def __init__(
        self,
        asr_model: str = None,
        open_asr: bool = None,
        open_tts: bool = None,
        tts_model: str = None,
    ):
        self.asr_model = asr_model
        self.open_asr = open_asr
        self.open_tts = open_tts
        self.tts_model = tts_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asr_model is not None:
            result['AsrModel'] = self.asr_model

        if self.open_asr is not None:
            result['OpenAsr'] = self.open_asr

        if self.open_tts is not None:
            result['OpenTts'] = self.open_tts

        if self.tts_model is not None:
            result['TtsModel'] = self.tts_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrModel') is not None:
            self.asr_model = m.get('AsrModel')

        if m.get('OpenAsr') is not None:
            self.open_asr = m.get('OpenAsr')

        if m.get('OpenTts') is not None:
            self.open_tts = m.get('OpenTts')

        if m.get('TtsModel') is not None:
            self.tts_model = m.get('TtsModel')

        return self

