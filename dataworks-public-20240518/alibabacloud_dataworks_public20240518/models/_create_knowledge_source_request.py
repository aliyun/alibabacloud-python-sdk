# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateKnowledgeSourceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        data_source: main_models.CreateKnowledgeSourceRequestDataSource = None,
        description: str = None,
        document: main_models.CreateKnowledgeSourceRequestDocument = None,
        knowledge_base_id: str = None,
        name: str = None,
        project: main_models.CreateKnowledgeSourceRequestProject = None,
        type: str = None,
    ):
        # The client token used to ensure idempotence.
        self.client_token = client_token
        # The data source configuration. This parameter is required when Type is set to DATA_SOURCE.
        self.data_source = data_source
        # The description.
        self.description = description
        # The document configuration. This parameter is required when Type is set to DOCUMENT.
        self.document = document
        # The ID of the knowledge base.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The name of the source.
        # 
        # This parameter is required.
        self.name = name
        # The project configuration. This parameter is required when Type is set to PROJECT.
        self.project = project
        # The type of the knowledge source. Valid values: PROJECT, DATA_SOURCE, and DOCUMENT.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.document:
            self.document.validate()
        if self.project:
            self.project.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.document is not None:
            result['Document'] = self.document.to_map()

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.name is not None:
            result['Name'] = self.name

        if self.project is not None:
            result['Project'] = self.project.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DataSource') is not None:
            temp_model = main_models.CreateKnowledgeSourceRequestDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Document') is not None:
            temp_model = main_models.CreateKnowledgeSourceRequestDocument()
            self.document = temp_model.from_map(m.get('Document'))

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Project') is not None:
            temp_model = main_models.CreateKnowledgeSourceRequestProject()
            self.project = temp_model.from_map(m.get('Project'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateKnowledgeSourceRequestProject(DaraModel):
    def __init__(
        self,
        env_type: str = None,
        project_id: int = None,
    ):
        # The environment type. This parameter is optional and restricts the read environment to Dev or Prod. If this parameter is not specified, it does not mean that you have the permissions to read data from both environments.
        self.env_type = env_type
        # The ID of the DataWorks workspace. This field is used to locate the source.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class CreateKnowledgeSourceRequestDocument(DaraModel):
    def __init__(
        self,
        connector_type: str = None,
        ding_talk: main_models.CreateKnowledgeSourceRequestDocumentDingTalk = None,
        feishu: main_models.CreateKnowledgeSourceRequestDocumentFeishu = None,
        lark: main_models.CreateKnowledgeSourceRequestDocumentLark = None,
        we_com: main_models.CreateKnowledgeSourceRequestDocumentWeCom = None,
        yuque: main_models.CreateKnowledgeSourceRequestDocumentYuque = None,
    ):
        # The type of the connector. Valid values: DINGTALK, FEISHU, LARK, WECOM, and YUQUE. The connector type cannot be changed after creation.
        self.connector_type = connector_type
        # The DingTalk configuration. This parameter is available only when ConnectorType is set to DINGTALK.
        self.ding_talk = ding_talk
        # The Feishu configuration. This parameter is available only when ConnectorType is set to FEISHU.
        self.feishu = feishu
        # The Lark configuration. This parameter is available only when ConnectorType is set to LARK.
        self.lark = lark
        # The WeCom configuration. This parameter is available only when ConnectorType is set to WECOM.
        self.we_com = we_com
        # The Yuque configuration. This parameter is available only when ConnectorType is set to YUQUE.
        self.yuque = yuque

    def validate(self):
        if self.ding_talk:
            self.ding_talk.validate()
        if self.feishu:
            self.feishu.validate()
        if self.lark:
            self.lark.validate()
        if self.we_com:
            self.we_com.validate()
        if self.yuque:
            self.yuque.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_type is not None:
            result['ConnectorType'] = self.connector_type

        if self.ding_talk is not None:
            result['DingTalk'] = self.ding_talk.to_map()

        if self.feishu is not None:
            result['Feishu'] = self.feishu.to_map()

        if self.lark is not None:
            result['Lark'] = self.lark.to_map()

        if self.we_com is not None:
            result['WeCom'] = self.we_com.to_map()

        if self.yuque is not None:
            result['Yuque'] = self.yuque.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorType') is not None:
            self.connector_type = m.get('ConnectorType')

        if m.get('DingTalk') is not None:
            temp_model = main_models.CreateKnowledgeSourceRequestDocumentDingTalk()
            self.ding_talk = temp_model.from_map(m.get('DingTalk'))

        if m.get('Feishu') is not None:
            temp_model = main_models.CreateKnowledgeSourceRequestDocumentFeishu()
            self.feishu = temp_model.from_map(m.get('Feishu'))

        if m.get('Lark') is not None:
            temp_model = main_models.CreateKnowledgeSourceRequestDocumentLark()
            self.lark = temp_model.from_map(m.get('Lark'))

        if m.get('WeCom') is not None:
            temp_model = main_models.CreateKnowledgeSourceRequestDocumentWeCom()
            self.we_com = temp_model.from_map(m.get('WeCom'))

        if m.get('Yuque') is not None:
            temp_model = main_models.CreateKnowledgeSourceRequestDocumentYuque()
            self.yuque = temp_model.from_map(m.get('Yuque'))

        return self

class CreateKnowledgeSourceRequestDocumentYuque(DaraModel):
    def __init__(
        self,
        teams: List[main_models.CreateKnowledgeSourceRequestDocumentYuqueTeams] = None,
    ):
        # The Yuque team configurations. Each team independently selects the synchronization scope.
        self.teams = teams

    def validate(self):
        if self.teams:
            for v1 in self.teams:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Teams'] = []
        if self.teams is not None:
            for k1 in self.teams:
                result['Teams'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.teams = []
        if m.get('Teams') is not None:
            for k1 in m.get('Teams'):
                temp_model = main_models.CreateKnowledgeSourceRequestDocumentYuqueTeams()
                self.teams.append(temp_model.from_map(k1))

        return self

class CreateKnowledgeSourceRequestDocumentYuqueTeams(DaraModel):
    def __init__(
        self,
        host: str = None,
        source_urls: List[str] = None,
        token: str = None,
    ):
        # The URL of the team site.
        self.host = host
        # The URLs of the knowledge bases, spaces, or documents selected for this connector. The actual allowed scope is determined by the connector and authorization settings.
        self.source_urls = source_urls
        # The access token for the Yuque team. This token is used only for creation or updates and is not returned in the response.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['Host'] = self.host

        if self.source_urls is not None:
            result['SourceUrls'] = self.source_urls

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('SourceUrls') is not None:
            self.source_urls = m.get('SourceUrls')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

class CreateKnowledgeSourceRequestDocumentWeCom(DaraModel):
    def __init__(
        self,
        bot_id: str = None,
        bot_secret: str = None,
        space_ids: List[str] = None,
    ):
        # The ID of the WeCom bot.
        self.bot_id = bot_id
        # The secret of the WeCom bot. This secret is used only for creation or updates and is not returned in the response.
        self.bot_secret = bot_secret
        # The IDs of the shared spaces selected for the WeCom connector.
        self.space_ids = space_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bot_id is not None:
            result['BotId'] = self.bot_id

        if self.bot_secret is not None:
            result['BotSecret'] = self.bot_secret

        if self.space_ids is not None:
            result['SpaceIds'] = self.space_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')

        if m.get('BotSecret') is not None:
            self.bot_secret = m.get('BotSecret')

        if m.get('SpaceIds') is not None:
            self.space_ids = m.get('SpaceIds')

        return self

class CreateKnowledgeSourceRequestDocumentLark(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret: str = None,
        source_urls: List[str] = None,
    ):
        # The ID of the Feishu or Lark application. This is not the AppSecret.
        self.app_id = app_id
        # The secret of the Feishu or Lark application. This secret is used only for creation or updates and is not returned in the response.
        self.app_secret = app_secret
        # The URLs of the knowledge bases, spaces, or documents selected for this connector. The actual allowed scope is determined by the connector and authorization settings.
        self.source_urls = source_urls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret

        if self.source_urls is not None:
            result['SourceUrls'] = self.source_urls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')

        if m.get('SourceUrls') is not None:
            self.source_urls = m.get('SourceUrls')

        return self

class CreateKnowledgeSourceRequestDocumentFeishu(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret: str = None,
        source_urls: List[str] = None,
    ):
        # The ID of the Feishu or Lark application. This is not the AppSecret.
        self.app_id = app_id
        # The secret of the Feishu or Lark application. This secret is used only for creation or updates and is not returned in the response.
        self.app_secret = app_secret
        # The URLs of the knowledge bases, spaces, or documents selected for this connector. The actual allowed scope is determined by the connector and authorization settings.
        self.source_urls = source_urls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret

        if self.source_urls is not None:
            result['SourceUrls'] = self.source_urls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')

        if m.get('SourceUrls') is not None:
            self.source_urls = m.get('SourceUrls')

        return self

class CreateKnowledgeSourceRequestDocumentDingTalk(DaraModel):
    def __init__(
        self,
        mcp_key: str = None,
        source_urls: List[str] = None,
    ):
        # The MCP authorization credential for the DingTalk document connector. This credential is used only for creation or updates and is not returned in the response.
        self.mcp_key = mcp_key
        # The URLs of the knowledge bases, spaces, or documents selected for this connector. The actual allowed scope is determined by the connector and authorization settings.
        self.source_urls = source_urls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mcp_key is not None:
            result['McpKey'] = self.mcp_key

        if self.source_urls is not None:
            result['SourceUrls'] = self.source_urls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('McpKey') is not None:
            self.mcp_key = m.get('McpKey')

        if m.get('SourceUrls') is not None:
            self.source_urls = m.get('SourceUrls')

        return self

class CreateKnowledgeSourceRequestDataSource(DaraModel):
    def __init__(
        self,
        data_source_id: int = None,
    ):
        # The ID of the DataWorks data source. The server uses this ID to resolve the associated workspace, environment, and data source type.
        self.data_source_id = data_source_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        return self

