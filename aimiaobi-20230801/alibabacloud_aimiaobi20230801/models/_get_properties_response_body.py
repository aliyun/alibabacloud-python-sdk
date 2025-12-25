# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetPropertiesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetPropertiesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.GetPropertiesResponseBodyData()
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

class GetPropertiesResponseBodyData(DaraModel):
    def __init__(
        self,
        chat_config: Dict[str, Any] = None,
        console_config: main_models.GetPropertiesResponseBodyDataConsoleConfig = None,
        general_config_map: Dict[str, Any] = None,
        intelligent_search_config: main_models.GetPropertiesResponseBodyDataIntelligentSearchConfig = None,
        miaosou_config: main_models.GetPropertiesResponseBodyDataMiaosouConfig = None,
        search_source_list: List[main_models.GetPropertiesResponseBodyDataSearchSourceList] = None,
        search_sources: List[main_models.GetPropertiesResponseBodyDataSearchSources] = None,
        slr_authorized: bool = None,
        user_info: main_models.GetPropertiesResponseBodyDataUserInfo = None,
        wanxiang_image_size_config: List[main_models.GetPropertiesResponseBodyDataWanxiangImageSizeConfig] = None,
        wanxiang_image_style_config: List[main_models.GetPropertiesResponseBodyDataWanxiangImageStyleConfig] = None,
    ):
        self.chat_config = chat_config
        self.console_config = console_config
        self.general_config_map = general_config_map
        self.intelligent_search_config = intelligent_search_config
        self.miaosou_config = miaosou_config
        self.search_source_list = search_source_list
        self.search_sources = search_sources
        self.slr_authorized = slr_authorized
        self.user_info = user_info
        self.wanxiang_image_size_config = wanxiang_image_size_config
        self.wanxiang_image_style_config = wanxiang_image_style_config

    def validate(self):
        if self.console_config:
            self.console_config.validate()
        if self.intelligent_search_config:
            self.intelligent_search_config.validate()
        if self.miaosou_config:
            self.miaosou_config.validate()
        if self.search_source_list:
            for v1 in self.search_source_list:
                 if v1:
                    v1.validate()
        if self.search_sources:
            for v1 in self.search_sources:
                 if v1:
                    v1.validate()
        if self.user_info:
            self.user_info.validate()
        if self.wanxiang_image_size_config:
            for v1 in self.wanxiang_image_size_config:
                 if v1:
                    v1.validate()
        if self.wanxiang_image_style_config:
            for v1 in self.wanxiang_image_style_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_config is not None:
            result['ChatConfig'] = self.chat_config

        if self.console_config is not None:
            result['ConsoleConfig'] = self.console_config.to_map()

        if self.general_config_map is not None:
            result['GeneralConfigMap'] = self.general_config_map

        if self.intelligent_search_config is not None:
            result['IntelligentSearchConfig'] = self.intelligent_search_config.to_map()

        if self.miaosou_config is not None:
            result['MiaosouConfig'] = self.miaosou_config.to_map()

        result['SearchSourceList'] = []
        if self.search_source_list is not None:
            for k1 in self.search_source_list:
                result['SearchSourceList'].append(k1.to_map() if k1 else None)

        result['SearchSources'] = []
        if self.search_sources is not None:
            for k1 in self.search_sources:
                result['SearchSources'].append(k1.to_map() if k1 else None)

        if self.slr_authorized is not None:
            result['SlrAuthorized'] = self.slr_authorized

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        result['WanxiangImageSizeConfig'] = []
        if self.wanxiang_image_size_config is not None:
            for k1 in self.wanxiang_image_size_config:
                result['WanxiangImageSizeConfig'].append(k1.to_map() if k1 else None)

        result['WanxiangImageStyleConfig'] = []
        if self.wanxiang_image_style_config is not None:
            for k1 in self.wanxiang_image_style_config:
                result['WanxiangImageStyleConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatConfig') is not None:
            self.chat_config = m.get('ChatConfig')

        if m.get('ConsoleConfig') is not None:
            temp_model = main_models.GetPropertiesResponseBodyDataConsoleConfig()
            self.console_config = temp_model.from_map(m.get('ConsoleConfig'))

        if m.get('GeneralConfigMap') is not None:
            self.general_config_map = m.get('GeneralConfigMap')

        if m.get('IntelligentSearchConfig') is not None:
            temp_model = main_models.GetPropertiesResponseBodyDataIntelligentSearchConfig()
            self.intelligent_search_config = temp_model.from_map(m.get('IntelligentSearchConfig'))

        if m.get('MiaosouConfig') is not None:
            temp_model = main_models.GetPropertiesResponseBodyDataMiaosouConfig()
            self.miaosou_config = temp_model.from_map(m.get('MiaosouConfig'))

        self.search_source_list = []
        if m.get('SearchSourceList') is not None:
            for k1 in m.get('SearchSourceList'):
                temp_model = main_models.GetPropertiesResponseBodyDataSearchSourceList()
                self.search_source_list.append(temp_model.from_map(k1))

        self.search_sources = []
        if m.get('SearchSources') is not None:
            for k1 in m.get('SearchSources'):
                temp_model = main_models.GetPropertiesResponseBodyDataSearchSources()
                self.search_sources.append(temp_model.from_map(k1))

        if m.get('SlrAuthorized') is not None:
            self.slr_authorized = m.get('SlrAuthorized')

        if m.get('UserInfo') is not None:
            temp_model = main_models.GetPropertiesResponseBodyDataUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        self.wanxiang_image_size_config = []
        if m.get('WanxiangImageSizeConfig') is not None:
            for k1 in m.get('WanxiangImageSizeConfig'):
                temp_model = main_models.GetPropertiesResponseBodyDataWanxiangImageSizeConfig()
                self.wanxiang_image_size_config.append(temp_model.from_map(k1))

        self.wanxiang_image_style_config = []
        if m.get('WanxiangImageStyleConfig') is not None:
            for k1 in m.get('WanxiangImageStyleConfig'):
                temp_model = main_models.GetPropertiesResponseBodyDataWanxiangImageStyleConfig()
                self.wanxiang_image_style_config.append(temp_model.from_map(k1))

        return self

class GetPropertiesResponseBodyDataWanxiangImageStyleConfig(DaraModel):
    def __init__(
        self,
        name: str = None,
        pic: str = None,
        value: str = None,
    ):
        self.name = name
        self.pic = pic
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.pic is not None:
            result['Pic'] = self.pic

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Pic') is not None:
            self.pic = m.get('Pic')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetPropertiesResponseBodyDataWanxiangImageSizeConfig(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetPropertiesResponseBodyDataUserInfo(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        tenant_id: str = None,
        user_id: str = None,
        username: str = None,
    ):
        self.agent_id = agent_id
        self.tenant_id = tenant_id
        self.user_id = user_id
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class GetPropertiesResponseBodyDataSearchSources(DaraModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        self.label = label
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetPropertiesResponseBodyDataSearchSourceList(DaraModel):
    def __init__(
        self,
        code: str = None,
        dataset_name: str = None,
        name: str = None,
    ):
        self.code = code
        self.dataset_name = dataset_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetPropertiesResponseBodyDataMiaosouConfig(DaraModel):
    def __init__(
        self,
        max_doc_size: int = None,
        model_infos: List[main_models.GetPropertiesResponseBodyDataMiaosouConfigModelInfos] = None,
        use_doc_size: int = None,
    ):
        self.max_doc_size = max_doc_size
        self.model_infos = model_infos
        self.use_doc_size = use_doc_size

    def validate(self):
        if self.model_infos:
            for v1 in self.model_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_doc_size is not None:
            result['MaxDocSize'] = self.max_doc_size

        result['ModelInfos'] = []
        if self.model_infos is not None:
            for k1 in self.model_infos:
                result['ModelInfos'].append(k1.to_map() if k1 else None)

        if self.use_doc_size is not None:
            result['UseDocSize'] = self.use_doc_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxDocSize') is not None:
            self.max_doc_size = m.get('MaxDocSize')

        self.model_infos = []
        if m.get('ModelInfos') is not None:
            for k1 in m.get('ModelInfos'):
                temp_model = main_models.GetPropertiesResponseBodyDataMiaosouConfigModelInfos()
                self.model_infos.append(temp_model.from_map(k1))

        if m.get('UseDocSize') is not None:
            self.use_doc_size = m.get('UseDocSize')

        return self

class GetPropertiesResponseBodyDataMiaosouConfigModelInfos(DaraModel):
    def __init__(
        self,
        model_id: str = None,
        model_name: str = None,
    ):
        self.model_id = model_id
        self.model_name = model_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        return self

class GetPropertiesResponseBodyDataIntelligentSearchConfig(DaraModel):
    def __init__(
        self,
        copilot_precise_search_sources: List[main_models.GetPropertiesResponseBodyDataIntelligentSearchConfigCopilotPreciseSearchSources] = None,
        product_description: str = None,
        search_samples: List[main_models.GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamples] = None,
        search_sources: List[main_models.GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSources] = None,
    ):
        self.copilot_precise_search_sources = copilot_precise_search_sources
        self.product_description = product_description
        self.search_samples = search_samples
        self.search_sources = search_sources

    def validate(self):
        if self.copilot_precise_search_sources:
            for v1 in self.copilot_precise_search_sources:
                 if v1:
                    v1.validate()
        if self.search_samples:
            for v1 in self.search_samples:
                 if v1:
                    v1.validate()
        if self.search_sources:
            for v1 in self.search_sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CopilotPreciseSearchSources'] = []
        if self.copilot_precise_search_sources is not None:
            for k1 in self.copilot_precise_search_sources:
                result['CopilotPreciseSearchSources'].append(k1.to_map() if k1 else None)

        if self.product_description is not None:
            result['ProductDescription'] = self.product_description

        result['SearchSamples'] = []
        if self.search_samples is not None:
            for k1 in self.search_samples:
                result['SearchSamples'].append(k1.to_map() if k1 else None)

        result['SearchSources'] = []
        if self.search_sources is not None:
            for k1 in self.search_sources:
                result['SearchSources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.copilot_precise_search_sources = []
        if m.get('CopilotPreciseSearchSources') is not None:
            for k1 in m.get('CopilotPreciseSearchSources'):
                temp_model = main_models.GetPropertiesResponseBodyDataIntelligentSearchConfigCopilotPreciseSearchSources()
                self.copilot_precise_search_sources.append(temp_model.from_map(k1))

        if m.get('ProductDescription') is not None:
            self.product_description = m.get('ProductDescription')

        self.search_samples = []
        if m.get('SearchSamples') is not None:
            for k1 in m.get('SearchSamples'):
                temp_model = main_models.GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamples()
                self.search_samples.append(temp_model.from_map(k1))

        self.search_sources = []
        if m.get('SearchSources') is not None:
            for k1 in m.get('SearchSources'):
                temp_model = main_models.GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSources()
                self.search_sources.append(temp_model.from_map(k1))

        return self

class GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSources(DaraModel):
    def __init__(
        self,
        code: str = None,
        dataset_name: str = None,
        name: str = None,
    ):
        self.code = code
        self.dataset_name = dataset_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamples(DaraModel):
    def __init__(
        self,
        articles: List[main_models.GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamplesArticles] = None,
        prompt: str = None,
        text: str = None,
    ):
        self.articles = articles
        self.prompt = prompt
        self.text = text

    def validate(self):
        if self.articles:
            for v1 in self.articles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Articles'] = []
        if self.articles is not None:
            for k1 in self.articles:
                result['Articles'].append(k1.to_map() if k1 else None)

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('Articles') is not None:
            for k1 in m.get('Articles'):
                temp_model = main_models.GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamplesArticles()
                self.articles.append(temp_model.from_map(k1))

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

class GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamplesArticles(DaraModel):
    def __init__(
        self,
        select: bool = None,
        stared: bool = None,
        title: str = None,
        url: str = None,
    ):
        self.select = select
        self.stared = stared
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.select is not None:
            result['Select'] = self.select

        if self.stared is not None:
            result['Stared'] = self.stared

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Select') is not None:
            self.select = m.get('Select')

        if m.get('Stared') is not None:
            self.stared = m.get('Stared')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetPropertiesResponseBodyDataIntelligentSearchConfigCopilotPreciseSearchSources(DaraModel):
    def __init__(
        self,
        code: str = None,
        dataset_name: str = None,
        name: str = None,
    ):
        self.code = code
        self.dataset_name = dataset_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetPropertiesResponseBodyDataConsoleConfig(DaraModel):
    def __init__(
        self,
        tip_content: str = None,
        title: str = None,
    ):
        self.tip_content = tip_content
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tip_content is not None:
            result['TipContent'] = self.tip_content

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TipContent') is not None:
            self.tip_content = m.get('TipContent')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

