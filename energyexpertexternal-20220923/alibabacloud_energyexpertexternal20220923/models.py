# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, BinaryIO, Any


class CarbonEmissionElecSummaryItem(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        name: str = None,
        ratio: float = None,
        raw_data: float = None,
    ):
        self.carbon_emission_data = carbon_emission_data
        self.data_unit = data_unit
        self.name = name
        self.ratio = ratio
        self.raw_data = raw_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.name is not None:
            result['name'] = self.name
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        return self


class ChatRefDocPostion(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['x'] = self.x
        if self.y is not None:
            result['y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')
        if m.get('y') is not None:
            self.y = m.get('y')
        return self


class ChatDocumentPageNum(TeaModel):
    def __init__(
        self,
        num: int = None,
        pos: List[List[ChatRefDocPostion]] = None,
    ):
        self.num = num
        self.pos = pos

    def validate(self):
        if self.pos:
            for k in self.pos:
                for k1 in k:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['num'] = self.num
        result['pos'] = []
        if self.pos is not None:
            for k in self.pos:
                l1 = []
                for k1 in k:
                    l1.append(k1.to_map() if k1 else None)
                result['pos'].append(l1)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('num') is not None:
            self.num = m.get('num')
        self.pos = []
        if m.get('pos') is not None:
            for k in m.get('pos'):
                l1 = []
                for k1 in k:
                    temp_model = ChatRefDocPostion()
                    l1.append(temp_model.from_map(k1))
                self.pos.append(l1)
        return self


class ChatRefDocPageInfo(TeaModel):
    def __init__(
        self,
        angle: float = None,
        excel_parse_result: str = None,
        image_height: int = None,
        image_url: str = None,
        image_width: int = None,
        page_id_cur_doc: int = None,
        pdf_parse_result: str = None,
        word_parse_result: str = None,
    ):
        self.angle = angle
        self.excel_parse_result = excel_parse_result
        self.image_height = image_height
        self.image_url = image_url
        self.image_width = image_width
        self.page_id_cur_doc = page_id_cur_doc
        self.pdf_parse_result = pdf_parse_result
        self.word_parse_result = word_parse_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['angle'] = self.angle
        if self.excel_parse_result is not None:
            result['excelParseResult'] = self.excel_parse_result
        if self.image_height is not None:
            result['imageHeight'] = self.image_height
        if self.image_url is not None:
            result['imageUrl'] = self.image_url
        if self.image_width is not None:
            result['imageWidth'] = self.image_width
        if self.page_id_cur_doc is not None:
            result['pageIdCurDoc'] = self.page_id_cur_doc
        if self.pdf_parse_result is not None:
            result['pdfParseResult'] = self.pdf_parse_result
        if self.word_parse_result is not None:
            result['wordParseResult'] = self.word_parse_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('angle') is not None:
            self.angle = m.get('angle')
        if m.get('excelParseResult') is not None:
            self.excel_parse_result = m.get('excelParseResult')
        if m.get('imageHeight') is not None:
            self.image_height = m.get('imageHeight')
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')
        if m.get('imageWidth') is not None:
            self.image_width = m.get('imageWidth')
        if m.get('pageIdCurDoc') is not None:
            self.page_id_cur_doc = m.get('pageIdCurDoc')
        if m.get('pdfParseResult') is not None:
            self.pdf_parse_result = m.get('pdfParseResult')
        if m.get('wordParseResult') is not None:
            self.word_parse_result = m.get('wordParseResult')
        return self


class ChatRefDocInfo(TeaModel):
    def __init__(
        self,
        page_list_info: List[ChatRefDocPageInfo] = None,
        pages: int = None,
    ):
        self.page_list_info = page_list_info
        self.pages = pages

    def validate(self):
        if self.page_list_info:
            for k in self.page_list_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['pageListInfo'] = []
        if self.page_list_info is not None:
            for k in self.page_list_info:
                result['pageListInfo'].append(k.to_map() if k else None)
        if self.pages is not None:
            result['pages'] = self.pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_list_info = []
        if m.get('pageListInfo') is not None:
            for k in m.get('pageListInfo'):
                temp_model = ChatRefDocPageInfo()
                self.page_list_info.append(temp_model.from_map(k))
        if m.get('pages') is not None:
            self.pages = m.get('pages')
        return self


class ChatRefDocItem(TeaModel):
    def __init__(
        self,
        doc_info: ChatRefDocInfo = None,
        doc_name: str = None,
        doc_url: str = None,
        origin_doc_name: str = None,
        origin_doc_url: str = None,
        page_num: List[ChatDocumentPageNum] = None,
        source_type: str = None,
    ):
        self.doc_info = doc_info
        self.doc_name = doc_name
        self.doc_url = doc_url
        self.origin_doc_name = origin_doc_name
        self.origin_doc_url = origin_doc_url
        self.page_num = page_num
        self.source_type = source_type

    def validate(self):
        if self.doc_info:
            self.doc_info.validate()
        if self.page_num:
            for k in self.page_num:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_info is not None:
            result['docInfo'] = self.doc_info.to_map()
        if self.doc_name is not None:
            result['docName'] = self.doc_name
        if self.doc_url is not None:
            result['docUrl'] = self.doc_url
        if self.origin_doc_name is not None:
            result['originDocName'] = self.origin_doc_name
        if self.origin_doc_url is not None:
            result['originDocUrl'] = self.origin_doc_url
        result['pageNum'] = []
        if self.page_num is not None:
            for k in self.page_num:
                result['pageNum'].append(k.to_map() if k else None)
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docInfo') is not None:
            temp_model = ChatRefDocInfo()
            self.doc_info = temp_model.from_map(m['docInfo'])
        if m.get('docName') is not None:
            self.doc_name = m.get('docName')
        if m.get('docUrl') is not None:
            self.doc_url = m.get('docUrl')
        if m.get('originDocName') is not None:
            self.origin_doc_name = m.get('originDocName')
        if m.get('originDocUrl') is not None:
            self.origin_doc_url = m.get('originDocUrl')
        self.page_num = []
        if m.get('pageNum') is not None:
            for k in m.get('pageNum'):
                temp_model = ChatDocumentPageNum()
                self.page_num.append(temp_model.from_map(k))
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        return self


class ChatItem(TeaModel):
    def __init__(
        self,
        answer: str = None,
        create_time: int = None,
        folder_id: str = None,
        folder_name: str = None,
        question: str = None,
        ref_doc_list: List[ChatRefDocItem] = None,
    ):
        self.answer = answer
        self.create_time = create_time
        self.folder_id = folder_id
        self.folder_name = folder_name
        self.question = question
        self.ref_doc_list = ref_doc_list

    def validate(self):
        if self.ref_doc_list:
            for k in self.ref_doc_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['answer'] = self.answer
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        if self.folder_name is not None:
            result['folderName'] = self.folder_name
        if self.question is not None:
            result['question'] = self.question
        result['refDocList'] = []
        if self.ref_doc_list is not None:
            for k in self.ref_doc_list:
                result['refDocList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answer') is not None:
            self.answer = m.get('answer')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        if m.get('folderName') is not None:
            self.folder_name = m.get('folderName')
        if m.get('question') is not None:
            self.question = m.get('question')
        self.ref_doc_list = []
        if m.get('refDocList') is not None:
            for k in m.get('refDocList'):
                temp_model = ChatRefDocItem()
                self.ref_doc_list.append(temp_model.from_map(k))
        return self


class ChatFolderItem(TeaModel):
    def __init__(
        self,
        folder_id: str = None,
        folder_name: str = None,
        sub_folders: List[ChatItem] = None,
    ):
        self.folder_id = folder_id
        self.folder_name = folder_name
        self.sub_folders = sub_folders

    def validate(self):
        if self.sub_folders:
            for k in self.sub_folders:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        if self.folder_name is not None:
            result['folderName'] = self.folder_name
        result['subFolders'] = []
        if self.sub_folders is not None:
            for k in self.sub_folders:
                result['subFolders'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        if m.get('folderName') is not None:
            self.folder_name = m.get('folderName')
        self.sub_folders = []
        if m.get('subFolders') is not None:
            for k in m.get('subFolders'):
                temp_model = ChatItem()
                self.sub_folders.append(temp_model.from_map(k))
        return self


class ChatRefDocPageNum(TeaModel):
    def __init__(
        self,
        num: int = None,
        pos: List[List[ChatRefDocPostion]] = None,
    ):
        self.num = num
        self.pos = pos

    def validate(self):
        if self.pos:
            for k in self.pos:
                for k1 in k:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['num'] = self.num
        result['pos'] = []
        if self.pos is not None:
            for k in self.pos:
                l1 = []
                for k1 in k:
                    l1.append(k1.to_map() if k1 else None)
                result['pos'].append(l1)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('num') is not None:
            self.num = m.get('num')
        self.pos = []
        if m.get('pos') is not None:
            for k in m.get('pos'):
                l1 = []
                for k1 in k:
                    temp_model = ChatRefDocPostion()
                    l1.append(temp_model.from_map(k1))
                self.pos.append(l1)
        return self


class ConstituteItemEnvGasEmissions(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        gas_emission_data: float = None,
        name: str = None,
        type: str = None,
    ):
        self.carbon_emission_data = carbon_emission_data
        self.gas_emission_data = gas_emission_data
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.gas_emission_data is not None:
            result['gasEmissionData'] = self.gas_emission_data
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('gasEmissionData') is not None:
            self.gas_emission_data = m.get('gasEmissionData')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ConstituteItem(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        emission_source: str = None,
        emission_source_key: str = None,
        enterprise_name: str = None,
        env_gas_emissions: List[ConstituteItemEnvGasEmissions] = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
        sub_constitute_items: List['ConstituteItem'] = None,
    ):
        self.carbon_emission_data = carbon_emission_data
        self.data_unit = data_unit
        self.emission_source = emission_source
        self.emission_source_key = emission_source_key
        self.enterprise_name = enterprise_name
        self.env_gas_emissions = env_gas_emissions
        self.name = name
        self.name_key = name_key
        self.ratio = ratio
        self.raw_data = raw_data
        self.sub_constitute_items = sub_constitute_items

    def validate(self):
        if self.env_gas_emissions:
            for k in self.env_gas_emissions:
                if k:
                    k.validate()
        if self.sub_constitute_items:
            for k in self.sub_constitute_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.emission_source is not None:
            result['emissionSource'] = self.emission_source
        if self.emission_source_key is not None:
            result['emissionSourceKey'] = self.emission_source_key
        if self.enterprise_name is not None:
            result['enterpriseName'] = self.enterprise_name
        result['envGasEmissions'] = []
        if self.env_gas_emissions is not None:
            for k in self.env_gas_emissions:
                result['envGasEmissions'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        result['subConstituteItems'] = []
        if self.sub_constitute_items is not None:
            for k in self.sub_constitute_items:
                result['subConstituteItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('emissionSource') is not None:
            self.emission_source = m.get('emissionSource')
        if m.get('emissionSourceKey') is not None:
            self.emission_source_key = m.get('emissionSourceKey')
        if m.get('enterpriseName') is not None:
            self.enterprise_name = m.get('enterpriseName')
        self.env_gas_emissions = []
        if m.get('envGasEmissions') is not None:
            for k in m.get('envGasEmissions'):
                temp_model = ConstituteItemEnvGasEmissions()
                self.env_gas_emissions.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        self.sub_constitute_items = []
        if m.get('subConstituteItems') is not None:
            for k in m.get('subConstituteItems'):
                temp_model = ConstituteItem()
                self.sub_constitute_items.append(temp_model.from_map(k))
        return self


class ContentItemExtInfoPos(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['x'] = self.x
        if self.y is not None:
            result['y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')
        if m.get('y') is not None:
            self.y = m.get('y')
        return self


class ContentItemExtInfo(TeaModel):
    def __init__(
        self,
        alignment: str = None,
        index: int = None,
        level: int = None,
        page_num: List[int] = None,
        pos: List[ContentItemExtInfoPos] = None,
        sub_type: str = None,
        text: str = None,
        type: str = None,
        unique_id: str = None,
    ):
        self.alignment = alignment
        self.index = index
        self.level = level
        self.page_num = page_num
        self.pos = pos
        self.sub_type = sub_type
        self.text = text
        self.type = type
        self.unique_id = unique_id

    def validate(self):
        if self.pos:
            for k in self.pos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alignment is not None:
            result['alignment'] = self.alignment
        if self.index is not None:
            result['index'] = self.index
        if self.level is not None:
            result['level'] = self.level
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        result['pos'] = []
        if self.pos is not None:
            for k in self.pos:
                result['pos'].append(k.to_map() if k else None)
        if self.sub_type is not None:
            result['subType'] = self.sub_type
        if self.text is not None:
            result['text'] = self.text
        if self.type is not None:
            result['type'] = self.type
        if self.unique_id is not None:
            result['uniqueId'] = self.unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alignment') is not None:
            self.alignment = m.get('alignment')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        self.pos = []
        if m.get('pos') is not None:
            for k in m.get('pos'):
                temp_model = ContentItemExtInfoPos()
                self.pos.append(temp_model.from_map(k))
        if m.get('subType') is not None:
            self.sub_type = m.get('subType')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('uniqueId') is not None:
            self.unique_id = m.get('uniqueId')
        return self


class ContentItem(TeaModel):
    def __init__(
        self,
        ext_info: List[ContentItemExtInfo] = None,
        score: float = None,
        text: str = None,
        type: str = None,
    ):
        self.ext_info = ext_info
        self.score = score
        self.text = text
        self.type = type

    def validate(self):
        if self.ext_info:
            for k in self.ext_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['extInfo'] = []
        if self.ext_info is not None:
            for k in self.ext_info:
                result['extInfo'].append(k.to_map() if k else None)
        if self.score is not None:
            result['score'] = self.score
        if self.text is not None:
            result['text'] = self.text
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ext_info = []
        if m.get('extInfo') is not None:
            for k in m.get('extInfo'):
                temp_model = ContentItemExtInfo()
                self.ext_info.append(temp_model.from_map(k))
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DocumentDetailItem(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        doc_hash: str = None,
        doc_name: str = None,
        doc_url: str = None,
        folder_id: str = None,
        folder_name: str = None,
        id: int = None,
        job_id: str = None,
        job_status: str = None,
        origin_doc_name: str = None,
        origin_doc_url: str = None,
        update_time: str = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.create_time = create_time
        self.doc_hash = doc_hash
        self.doc_name = doc_name
        self.doc_url = doc_url
        self.folder_id = folder_id
        self.folder_name = folder_name
        self.id = id
        self.job_id = job_id
        self.job_status = job_status
        self.origin_doc_name = origin_doc_name
        self.origin_doc_url = origin_doc_url
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.doc_hash is not None:
            result['docHash'] = self.doc_hash
        if self.doc_name is not None:
            result['docName'] = self.doc_name
        if self.doc_url is not None:
            result['docUrl'] = self.doc_url
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        if self.folder_name is not None:
            result['folderName'] = self.folder_name
        if self.id is not None:
            result['id'] = self.id
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.job_status is not None:
            result['jobStatus'] = self.job_status
        if self.origin_doc_name is not None:
            result['originDocName'] = self.origin_doc_name
        if self.origin_doc_url is not None:
            result['originDocUrl'] = self.origin_doc_url
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('docHash') is not None:
            self.doc_hash = m.get('docHash')
        if m.get('docName') is not None:
            self.doc_name = m.get('docName')
        if m.get('docUrl') is not None:
            self.doc_url = m.get('docUrl')
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        if m.get('folderName') is not None:
            self.folder_name = m.get('folderName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')
        if m.get('originDocName') is not None:
            self.origin_doc_name = m.get('originDocName')
        if m.get('originDocUrl') is not None:
            self.origin_doc_url = m.get('originDocUrl')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class EpdInventoryConstituteItem(TeaModel):
    def __init__(
        self,
        carbon_emission: float = None,
        factor: str = None,
        factor_dataset: str = None,
        factor_id: str = None,
        factor_type: int = None,
        factor_unit: str = None,
        inventory_id: int = None,
        inventory_unit: str = None,
        inventory_value: float = None,
        inventory_value_per_product: float = None,
        inventory_value_per_product_unit: str = None,
        items: List['EpdInventoryConstituteItem'] = None,
        name: str = None,
        num: int = None,
        percent: float = None,
        quantity: float = None,
        resource_type: str = None,
        state: int = None,
        unit: str = None,
    ):
        self.carbon_emission = carbon_emission
        self.factor = factor
        self.factor_dataset = factor_dataset
        self.factor_id = factor_id
        self.factor_type = factor_type
        self.factor_unit = factor_unit
        self.inventory_id = inventory_id
        self.inventory_unit = inventory_unit
        self.inventory_value = inventory_value
        self.inventory_value_per_product = inventory_value_per_product
        self.inventory_value_per_product_unit = inventory_value_per_product_unit
        self.items = items
        self.name = name
        self.num = num
        self.percent = percent
        self.quantity = quantity
        self.resource_type = resource_type
        self.state = state
        self.unit = unit

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission
        if self.factor is not None:
            result['factor'] = self.factor
        if self.factor_dataset is not None:
            result['factorDataset'] = self.factor_dataset
        if self.factor_id is not None:
            result['factorId'] = self.factor_id
        if self.factor_type is not None:
            result['factorType'] = self.factor_type
        if self.factor_unit is not None:
            result['factorUnit'] = self.factor_unit
        if self.inventory_id is not None:
            result['inventoryId'] = self.inventory_id
        if self.inventory_unit is not None:
            result['inventoryUnit'] = self.inventory_unit
        if self.inventory_value is not None:
            result['inventoryValue'] = self.inventory_value
        if self.inventory_value_per_product is not None:
            result['inventoryValuePerProduct'] = self.inventory_value_per_product
        if self.inventory_value_per_product_unit is not None:
            result['inventoryValuePerProductUnit'] = self.inventory_value_per_product_unit
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.num is not None:
            result['num'] = self.num
        if self.percent is not None:
            result['percent'] = self.percent
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.state is not None:
            result['state'] = self.state
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')
        if m.get('factor') is not None:
            self.factor = m.get('factor')
        if m.get('factorDataset') is not None:
            self.factor_dataset = m.get('factorDataset')
        if m.get('factorId') is not None:
            self.factor_id = m.get('factorId')
        if m.get('factorType') is not None:
            self.factor_type = m.get('factorType')
        if m.get('factorUnit') is not None:
            self.factor_unit = m.get('factorUnit')
        if m.get('inventoryId') is not None:
            self.inventory_id = m.get('inventoryId')
        if m.get('inventoryUnit') is not None:
            self.inventory_unit = m.get('inventoryUnit')
        if m.get('inventoryValue') is not None:
            self.inventory_value = m.get('inventoryValue')
        if m.get('inventoryValuePerProduct') is not None:
            self.inventory_value_per_product = m.get('inventoryValuePerProduct')
        if m.get('inventoryValuePerProductUnit') is not None:
            self.inventory_value_per_product_unit = m.get('inventoryValuePerProductUnit')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = EpdInventoryConstituteItem()
                self.items.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('num') is not None:
            self.num = m.get('num')
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class FolderItem(TeaModel):
    def __init__(
        self,
        current_level: int = None,
        doc_count: int = None,
        folder_default: int = None,
        folder_id: str = None,
        folder_name: str = None,
        folder_num: int = None,
        oss_domain: str = None,
        oss_path: str = None,
        oss_update_by: str = None,
        parent_folder_id: str = None,
        resource_path: str = None,
        storage_type: int = None,
        sub_folder_list: List['FolderItem'] = None,
        sync_parsing_status: int = None,
        sync_status: int = None,
        task_id: int = None,
    ):
        self.current_level = current_level
        self.doc_count = doc_count
        self.folder_default = folder_default
        self.folder_id = folder_id
        self.folder_name = folder_name
        self.folder_num = folder_num
        self.oss_domain = oss_domain
        self.oss_path = oss_path
        self.oss_update_by = oss_update_by
        self.parent_folder_id = parent_folder_id
        self.resource_path = resource_path
        self.storage_type = storage_type
        self.sub_folder_list = sub_folder_list
        self.sync_parsing_status = sync_parsing_status
        self.sync_status = sync_status
        self.task_id = task_id

    def validate(self):
        if self.sub_folder_list:
            for k in self.sub_folder_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_level is not None:
            result['currentLevel'] = self.current_level
        if self.doc_count is not None:
            result['docCount'] = self.doc_count
        if self.folder_default is not None:
            result['folderDefault'] = self.folder_default
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        if self.folder_name is not None:
            result['folderName'] = self.folder_name
        if self.folder_num is not None:
            result['folderNum'] = self.folder_num
        if self.oss_domain is not None:
            result['ossDomain'] = self.oss_domain
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.oss_update_by is not None:
            result['ossUpdateBy'] = self.oss_update_by
        if self.parent_folder_id is not None:
            result['parentFolderId'] = self.parent_folder_id
        if self.resource_path is not None:
            result['resourcePath'] = self.resource_path
        if self.storage_type is not None:
            result['storageType'] = self.storage_type
        result['subFolderList'] = []
        if self.sub_folder_list is not None:
            for k in self.sub_folder_list:
                result['subFolderList'].append(k.to_map() if k else None)
        if self.sync_parsing_status is not None:
            result['syncParsingStatus'] = self.sync_parsing_status
        if self.sync_status is not None:
            result['syncStatus'] = self.sync_status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentLevel') is not None:
            self.current_level = m.get('currentLevel')
        if m.get('docCount') is not None:
            self.doc_count = m.get('docCount')
        if m.get('folderDefault') is not None:
            self.folder_default = m.get('folderDefault')
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        if m.get('folderName') is not None:
            self.folder_name = m.get('folderName')
        if m.get('folderNum') is not None:
            self.folder_num = m.get('folderNum')
        if m.get('ossDomain') is not None:
            self.oss_domain = m.get('ossDomain')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('ossUpdateBy') is not None:
            self.oss_update_by = m.get('ossUpdateBy')
        if m.get('parentFolderId') is not None:
            self.parent_folder_id = m.get('parentFolderId')
        if m.get('resourcePath') is not None:
            self.resource_path = m.get('resourcePath')
        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')
        self.sub_folder_list = []
        if m.get('subFolderList') is not None:
            for k in m.get('subFolderList'):
                temp_model = FolderItem()
                self.sub_folder_list.append(temp_model.from_map(k))
        if m.get('syncParsingStatus') is not None:
            self.sync_parsing_status = m.get('syncParsingStatus')
        if m.get('syncStatus') is not None:
            self.sync_status = m.get('syncStatus')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GwpResourceConstitute(TeaModel):
    def __init__(
        self,
        carbon_emission: float = None,
        name: str = None,
        percent: str = None,
        resource_type: int = None,
        unit: str = None,
    ):
        self.carbon_emission = carbon_emission
        self.name = name
        self.percent = percent
        self.resource_type = resource_type
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission
        if self.name is not None:
            result['name'] = self.name
        if self.percent is not None:
            result['percent'] = self.percent
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GwpInventoryConstitute(TeaModel):
    def __init__(
        self,
        by_resource_type: List[GwpResourceConstitute] = None,
        carbon_emission: float = None,
        items: List['GwpInventoryConstitute'] = None,
        name: str = None,
        percent: float = None,
        resource_type: int = None,
        unit: str = None,
    ):
        self.by_resource_type = by_resource_type
        self.carbon_emission = carbon_emission
        self.items = items
        self.name = name
        self.percent = percent
        self.resource_type = resource_type
        self.unit = unit

    def validate(self):
        if self.by_resource_type:
            for k in self.by_resource_type:
                if k:
                    k.validate()
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['byResourceType'] = []
        if self.by_resource_type is not None:
            for k in self.by_resource_type:
                result['byResourceType'].append(k.to_map() if k else None)
        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.percent is not None:
            result['percent'] = self.percent
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.by_resource_type = []
        if m.get('byResourceType') is not None:
            for k in m.get('byResourceType'):
                temp_model = GwpResourceConstitute()
                self.by_resource_type.append(temp_model.from_map(k))
        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = GwpInventoryConstitute()
                self.items.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class OrgEmissionModuleEmissionList(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
    ):
        self.carbon_emission_data = carbon_emission_data
        self.name = name
        self.name_key = name_key
        self.ratio = ratio

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        return self


class OrgEmission(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        module_emission_list: List[OrgEmissionModuleEmissionList] = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        sub_emission_items: List['OrgEmission'] = None,
        weighting_carbon_emission_data: float = None,
        weighting_proportion: float = None,
        weighting_ratio: float = None,
    ):
        self.carbon_emission_data = carbon_emission_data
        self.module_emission_list = module_emission_list
        self.name = name
        self.name_key = name_key
        self.ratio = ratio
        self.sub_emission_items = sub_emission_items
        self.weighting_carbon_emission_data = weighting_carbon_emission_data
        self.weighting_proportion = weighting_proportion
        self.weighting_ratio = weighting_ratio

    def validate(self):
        if self.module_emission_list:
            for k in self.module_emission_list:
                if k:
                    k.validate()
        if self.sub_emission_items:
            for k in self.sub_emission_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        result['moduleEmissionList'] = []
        if self.module_emission_list is not None:
            for k in self.module_emission_list:
                result['moduleEmissionList'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        result['subEmissionItems'] = []
        if self.sub_emission_items is not None:
            for k in self.sub_emission_items:
                result['subEmissionItems'].append(k.to_map() if k else None)
        if self.weighting_carbon_emission_data is not None:
            result['weightingCarbonEmissionData'] = self.weighting_carbon_emission_data
        if self.weighting_proportion is not None:
            result['weightingProportion'] = self.weighting_proportion
        if self.weighting_ratio is not None:
            result['weightingRatio'] = self.weighting_ratio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        self.module_emission_list = []
        if m.get('moduleEmissionList') is not None:
            for k in m.get('moduleEmissionList'):
                temp_model = OrgEmissionModuleEmissionList()
                self.module_emission_list.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        self.sub_emission_items = []
        if m.get('subEmissionItems') is not None:
            for k in m.get('subEmissionItems'):
                temp_model = OrgEmission()
                self.sub_emission_items.append(temp_model.from_map(k))
        if m.get('weightingCarbonEmissionData') is not None:
            self.weighting_carbon_emission_data = m.get('weightingCarbonEmissionData')
        if m.get('weightingProportion') is not None:
            self.weighting_proportion = m.get('weightingProportion')
        if m.get('weightingRatio') is not None:
            self.weighting_ratio = m.get('weightingRatio')
        return self


class AddFolderRequest(TeaModel):
    def __init__(
        self,
        folder_name: str = None,
        parent_folder_id: str = None,
    ):
        # This parameter is required.
        self.folder_name = folder_name
        # This parameter is required.
        self.parent_folder_id = parent_folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_name is not None:
            result['folderName'] = self.folder_name
        if self.parent_folder_id is not None:
            result['parentFolderId'] = self.parent_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('folderName') is not None:
            self.folder_name = m.get('folderName')
        if m.get('parentFolderId') is not None:
            self.parent_folder_id = m.get('parentFolderId')
        return self


class AddFolderResponseBody(TeaModel):
    def __init__(
        self,
        data: FolderItem = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = FolderItem()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AddFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddFolderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AnalyzeVlRealtimeRequest(TeaModel):
    def __init__(
        self,
        file_url: str = None,
        language: str = None,
        template_id: str = None,
    ):
        # Choose one of fileUrl or fileUrlObject:
        # 
        # - fileUrl: Use in the form of a document URL, for a single document (supports up to 1000 pages and 100MB)
        # 
        # - fileUrlObject: Use when calling the interface with local file upload, for a single document (supports up to 1000 pages and 100 MB)
        # 
        # > The relationship between file parsing methods and supported document types
        # > - Long Text RAG: Supports pdf, doc/docx, up to 1000 pages
        # > - Image Processing: Supports pdf, jpg, jpeg, png, bmp
        # > - Long Text Understanding: Supports pdf, doc/docx, xls/xlsx
        self.file_url = file_url
        # Language, parameters that can be passed
        # - zh-CN: Chinese (default)
        # - en-US: English
        self.language = language
        # A unique parsing template ID used to specify the key-value pairs to be extracted from the document. You need to log in to the template management page, configure the template, and then get the corresponding template ID.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['fileUrl'] = self.file_url
        if self.language is not None:
            result['language'] = self.language
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class AnalyzeVlRealtimeAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_url_object: BinaryIO = None,
        language: str = None,
        template_id: str = None,
    ):
        # Choose one of fileUrl or fileUrlObject:
        # 
        # - fileUrl: Use in the form of a document URL, for a single document (supports up to 1000 pages and 100MB)
        # 
        # - fileUrlObject: Use when calling the interface with local file upload, for a single document (supports up to 1000 pages and 100 MB)
        # 
        # > The relationship between file parsing methods and supported document types
        # > - Long Text RAG: Supports pdf, doc/docx, up to 1000 pages
        # > - Image Processing: Supports pdf, jpg, jpeg, png, bmp
        # > - Long Text Understanding: Supports pdf, doc/docx, xls/xlsx
        self.file_url_object = file_url_object
        # Language, parameters that can be passed
        # - zh-CN: Chinese (default)
        # - en-US: English
        self.language = language
        # A unique parsing template ID used to specify the key-value pairs to be extracted from the document. You need to log in to the template management page, configure the template, and then get the corresponding template ID.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url_object is not None:
            result['fileUrl'] = self.file_url_object
        if self.language is not None:
            result['language'] = self.language
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileUrl') is not None:
            self.file_url_object = m.get('fileUrl')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class AnalyzeVlRealtimeResponseBodyDataKvListInfoContextConfidence(TeaModel):
    def __init__(
        self,
        key_confidence: float = None,
        value_confidence: float = None,
    ):
        # Key confidence
        self.key_confidence = key_confidence
        # Value confidence
        self.value_confidence = value_confidence

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_confidence is not None:
            result['keyConfidence'] = self.key_confidence
        if self.value_confidence is not None:
            result['valueConfidence'] = self.value_confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyConfidence') is not None:
            self.key_confidence = m.get('keyConfidence')
        if m.get('valueConfidence') is not None:
            self.value_confidence = m.get('valueConfidence')
        return self


class AnalyzeVlRealtimeResponseBodyDataKvListInfoContext(TeaModel):
    def __init__(
        self,
        confidence: AnalyzeVlRealtimeResponseBodyDataKvListInfoContextConfidence = None,
        key: List[ContentItem] = None,
        value: List[ContentItem] = None,
    ):
        # Confidence
        self.confidence = confidence
        # Key recall information details
        self.key = key
        # Value recall information details
        self.value = value

    def validate(self):
        if self.confidence:
            self.confidence.validate()
        if self.key:
            for k in self.key:
                if k:
                    k.validate()
        if self.value:
            for k in self.value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['confidence'] = self.confidence.to_map()
        result['key'] = []
        if self.key is not None:
            for k in self.key:
                result['key'].append(k.to_map() if k else None)
        result['value'] = []
        if self.value is not None:
            for k in self.value:
                result['value'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('confidence') is not None:
            temp_model = AnalyzeVlRealtimeResponseBodyDataKvListInfoContextConfidence()
            self.confidence = temp_model.from_map(m['confidence'])
        self.key = []
        if m.get('key') is not None:
            for k in m.get('key'):
                temp_model = ContentItem()
                self.key.append(temp_model.from_map(k))
        self.value = []
        if m.get('value') is not None:
            for k in m.get('value'):
                temp_model = ContentItem()
                self.value.append(temp_model.from_map(k))
        return self


class AnalyzeVlRealtimeResponseBodyDataKvListInfo(TeaModel):
    def __init__(
        self,
        context: AnalyzeVlRealtimeResponseBodyDataKvListInfoContext = None,
        key_name: str = None,
        key_value: str = None,
    ):
        # Recall content
        self.context = context
        # Field Key name
        self.key_name = key_name
        # Field key value
        self.key_value = key_value

    def validate(self):
        if self.context:
            self.context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['context'] = self.context.to_map()
        if self.key_name is not None:
            result['keyName'] = self.key_name
        if self.key_value is not None:
            result['keyValue'] = self.key_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('context') is not None:
            temp_model = AnalyzeVlRealtimeResponseBodyDataKvListInfoContext()
            self.context = temp_model.from_map(m['context'])
        if m.get('keyName') is not None:
            self.key_name = m.get('keyName')
        if m.get('keyValue') is not None:
            self.key_value = m.get('keyValue')
        return self


class AnalyzeVlRealtimeResponseBodyData(TeaModel):
    def __init__(
        self,
        kv_list_info: List[AnalyzeVlRealtimeResponseBodyDataKvListInfo] = None,
    ):
        # Document parsing result details
        self.kv_list_info = kv_list_info

    def validate(self):
        if self.kv_list_info:
            for k in self.kv_list_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['kvListInfo'] = []
        if self.kv_list_info is not None:
            for k in self.kv_list_info:
                result['kvListInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kv_list_info = []
        if m.get('kvListInfo') is not None:
            for k in m.get('kvListInfo'):
                temp_model = AnalyzeVlRealtimeResponseBodyDataKvListInfo()
                self.kv_list_info.append(temp_model.from_map(k))
        return self


class AnalyzeVlRealtimeResponseBody(TeaModel):
    def __init__(
        self,
        data: AnalyzeVlRealtimeResponseBodyData = None,
        request_id: str = None,
    ):
        # Return result.
        self.data = data
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = AnalyzeVlRealtimeResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AnalyzeVlRealtimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AnalyzeVlRealtimeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AnalyzeVlRealtimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSaveInstructionStatusRequest(TeaModel):
    def __init__(
        self,
        factory_id: str = None,
        p_key: str = None,
        status_list: str = None,
    ):
        # This parameter is required.
        self.factory_id = factory_id
        self.p_key = p_key
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id
        if self.p_key is not None:
            result['pKey'] = self.p_key
        if self.status_list is not None:
            result['statusList'] = self.status_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')
        if m.get('pKey') is not None:
            self.p_key = m.get('pKey')
        if m.get('statusList') is not None:
            self.status_list = m.get('statusList')
        return self


class BatchSaveInstructionStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        # true
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class BatchSaveInstructionStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchSaveInstructionStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchSaveInstructionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUpdateSystemRunningPlanRequest(TeaModel):
    def __init__(
        self,
        control_type: int = None,
        date_type: int = None,
        earliest_startup_time: str = None,
        end_time: str = None,
        factory_id: str = None,
        latest_shutdown_time: str = None,
        max_carbon_dioxide: float = None,
        max_tem: float = None,
        min_tem: float = None,
        season_mode: int = None,
        start_time: str = None,
        system_id: str = None,
        working_end_time: str = None,
        working_start_time: str = None,
    ):
        self.control_type = control_type
        self.date_type = date_type
        self.earliest_startup_time = earliest_startup_time
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.factory_id = factory_id
        self.latest_shutdown_time = latest_shutdown_time
        self.max_carbon_dioxide = max_carbon_dioxide
        self.max_tem = max_tem
        self.min_tem = min_tem
        self.season_mode = season_mode
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.system_id = system_id
        self.working_end_time = working_end_time
        self.working_start_time = working_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_type is not None:
            result['controlType'] = self.control_type
        if self.date_type is not None:
            result['dateType'] = self.date_type
        if self.earliest_startup_time is not None:
            result['earliestStartupTime'] = self.earliest_startup_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id
        if self.latest_shutdown_time is not None:
            result['latestShutdownTime'] = self.latest_shutdown_time
        if self.max_carbon_dioxide is not None:
            result['maxCarbonDioxide'] = self.max_carbon_dioxide
        if self.max_tem is not None:
            result['maxTem'] = self.max_tem
        if self.min_tem is not None:
            result['minTem'] = self.min_tem
        if self.season_mode is not None:
            result['seasonMode'] = self.season_mode
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.system_id is not None:
            result['systemId'] = self.system_id
        if self.working_end_time is not None:
            result['workingEndTime'] = self.working_end_time
        if self.working_start_time is not None:
            result['workingStartTime'] = self.working_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('controlType') is not None:
            self.control_type = m.get('controlType')
        if m.get('dateType') is not None:
            self.date_type = m.get('dateType')
        if m.get('earliestStartupTime') is not None:
            self.earliest_startup_time = m.get('earliestStartupTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')
        if m.get('latestShutdownTime') is not None:
            self.latest_shutdown_time = m.get('latestShutdownTime')
        if m.get('maxCarbonDioxide') is not None:
            self.max_carbon_dioxide = m.get('maxCarbonDioxide')
        if m.get('maxTem') is not None:
            self.max_tem = m.get('maxTem')
        if m.get('minTem') is not None:
            self.min_tem = m.get('minTem')
        if m.get('seasonMode') is not None:
            self.season_mode = m.get('seasonMode')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('systemId') is not None:
            self.system_id = m.get('systemId')
        if m.get('workingEndTime') is not None:
            self.working_end_time = m.get('workingEndTime')
        if m.get('workingStartTime') is not None:
            self.working_start_time = m.get('workingStartTime')
        return self


class BatchUpdateSystemRunningPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class BatchUpdateSystemRunningPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchUpdateSystemRunningPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchUpdateSystemRunningPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatRequest(TeaModel):
    def __init__(
        self,
        question: str = None,
        session_id: str = None,
    ):
        # Q&A content.
        # 
        # This parameter is required.
        self.question = question
        # - Q&A session ID.
        # - Historical sessions can be retrieved through GetSessionList.
        # - A new session can also be created via CreateChatSession.
        # 
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.question is not None:
            result['question'] = self.question
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('question') is not None:
            self.question = m.get('question')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class ChatResponseBody(TeaModel):
    def __init__(
        self,
        data: ChatItem = None,
        request_id: str = None,
    ):
        # Details of the Q&A.
        self.data = data
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ChatItem()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ChatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatStreamRequest(TeaModel):
    def __init__(
        self,
        question: str = None,
        session_id: str = None,
    ):
        # Q&A content.
        # 
        # This parameter is required.
        self.question = question
        # - Q&A session ID.
        # - Historical sessions can be retrieved through GetSessionList.
        # - A new session can also be created via CreateChatSession.
        # 
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.question is not None:
            result['question'] = self.question
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('question') is not None:
            self.question = m.get('question')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class ChatStreamResponseBody(TeaModel):
    def __init__(
        self,
        data: ChatItem = None,
        request_id: str = None,
    ):
        # Q&A content.
        self.data = data
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ChatItem()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ChatStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatStreamResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChatSessionRequest(TeaModel):
    def __init__(
        self,
        folder_id: str = None,
        name: str = None,
        user_id: str = None,
    ):
        # Folder ID, to search for Q&A content within the current folder and its subfolders.
        # 
        # This parameter is required.
        self.folder_id = folder_id
        # Name of the current session.
        # 
        # This parameter is required.
        self.name = name
        # The unique identifier of the user. If not provided, the SDK calling account will be used as the user ID by default.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateChatSessionResponseBodyData(TeaModel):
    def __init__(
        self,
        session_id: str = None,
    ):
        # Q&A session ID, used to record multiple Q&A sessions of the same user.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class CreateChatSessionResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateChatSessionResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned data structure.
        self.data = data
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateChatSessionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateChatSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateChatSessionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateChatSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDocumentRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class DeleteDocumentResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        # Returns true on success, false otherwise
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDocumentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFolderRequest(TeaModel):
    def __init__(
        self,
        folder_id: str = None,
    ):
        self.folder_id = folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        return self


class DeleteFolderResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFolderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetailDocumentRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class DetailDocumentResponseBody(TeaModel):
    def __init__(
        self,
        data: DocumentDetailItem = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DocumentDetailItem()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DetailDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetailDocumentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetailDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditProhibitedDevicesRequestHvacDeviceConfigVOList(TeaModel):
    def __init__(
        self,
        building_id: str = None,
        device_id: str = None,
        device_name: str = None,
        device_type: str = None,
        fence_id: str = None,
        floor_id: str = None,
        is_forbidden: int = None,
        is_unfavorable_area: int = None,
    ):
        self.building_id = building_id
        self.device_id = device_id
        self.device_name = device_name
        # This parameter is required.
        self.device_type = device_type
        self.fence_id = fence_id
        self.floor_id = floor_id
        # This parameter is required.
        self.is_forbidden = is_forbidden
        self.is_unfavorable_area = is_unfavorable_area

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.building_id is not None:
            result['buildingId'] = self.building_id
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.device_type is not None:
            result['deviceType'] = self.device_type
        if self.fence_id is not None:
            result['fenceId'] = self.fence_id
        if self.floor_id is not None:
            result['floorId'] = self.floor_id
        if self.is_forbidden is not None:
            result['isForbidden'] = self.is_forbidden
        if self.is_unfavorable_area is not None:
            result['isUnfavorableArea'] = self.is_unfavorable_area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildingId') is not None:
            self.building_id = m.get('buildingId')
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('deviceType') is not None:
            self.device_type = m.get('deviceType')
        if m.get('fenceId') is not None:
            self.fence_id = m.get('fenceId')
        if m.get('floorId') is not None:
            self.floor_id = m.get('floorId')
        if m.get('isForbidden') is not None:
            self.is_forbidden = m.get('isForbidden')
        if m.get('isUnfavorableArea') is not None:
            self.is_unfavorable_area = m.get('isUnfavorableArea')
        return self


class EditProhibitedDevicesRequest(TeaModel):
    def __init__(
        self,
        factory_id: str = None,
        hvac_device_config_volist: List[EditProhibitedDevicesRequestHvacDeviceConfigVOList] = None,
        system_id: str = None,
    ):
        # This parameter is required.
        self.factory_id = factory_id
        # This parameter is required.
        self.hvac_device_config_volist = hvac_device_config_volist
        # This parameter is required.
        self.system_id = system_id

    def validate(self):
        if self.hvac_device_config_volist:
            for k in self.hvac_device_config_volist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id
        result['hvacDeviceConfigVOList'] = []
        if self.hvac_device_config_volist is not None:
            for k in self.hvac_device_config_volist:
                result['hvacDeviceConfigVOList'].append(k.to_map() if k else None)
        if self.system_id is not None:
            result['systemId'] = self.system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')
        self.hvac_device_config_volist = []
        if m.get('hvacDeviceConfigVOList') is not None:
            for k in m.get('hvacDeviceConfigVOList'):
                temp_model = EditProhibitedDevicesRequestHvacDeviceConfigVOList()
                self.hvac_device_config_volist.append(temp_model.from_map(k))
        if m.get('systemId') is not None:
            self.system_id = m.get('systemId')
        return self


class EditProhibitedDevicesResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class EditProhibitedDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EditProhibitedDevicesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EditProhibitedDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditUnfavorableAreaDevicesRequestHvacDeviceConfigVOList(TeaModel):
    def __init__(
        self,
        building_id: str = None,
        device_id: str = None,
        device_name: str = None,
        device_type: str = None,
        fence_id: str = None,
        floor_id: str = None,
        is_forbidden: int = None,
        is_unfavorable_area: int = None,
    ):
        self.building_id = building_id
        self.device_id = device_id
        self.device_name = device_name
        # This parameter is required.
        self.device_type = device_type
        self.fence_id = fence_id
        self.floor_id = floor_id
        self.is_forbidden = is_forbidden
        # This parameter is required.
        self.is_unfavorable_area = is_unfavorable_area

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.building_id is not None:
            result['buildingId'] = self.building_id
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.device_type is not None:
            result['deviceType'] = self.device_type
        if self.fence_id is not None:
            result['fenceId'] = self.fence_id
        if self.floor_id is not None:
            result['floorId'] = self.floor_id
        if self.is_forbidden is not None:
            result['isForbidden'] = self.is_forbidden
        if self.is_unfavorable_area is not None:
            result['isUnfavorableArea'] = self.is_unfavorable_area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildingId') is not None:
            self.building_id = m.get('buildingId')
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('deviceType') is not None:
            self.device_type = m.get('deviceType')
        if m.get('fenceId') is not None:
            self.fence_id = m.get('fenceId')
        if m.get('floorId') is not None:
            self.floor_id = m.get('floorId')
        if m.get('isForbidden') is not None:
            self.is_forbidden = m.get('isForbidden')
        if m.get('isUnfavorableArea') is not None:
            self.is_unfavorable_area = m.get('isUnfavorableArea')
        return self


class EditUnfavorableAreaDevicesRequest(TeaModel):
    def __init__(
        self,
        factory_id: str = None,
        hvac_device_config_volist: List[EditUnfavorableAreaDevicesRequestHvacDeviceConfigVOList] = None,
        system_id: str = None,
    ):
        # This parameter is required.
        self.factory_id = factory_id
        # This parameter is required.
        self.hvac_device_config_volist = hvac_device_config_volist
        # This parameter is required.
        self.system_id = system_id

    def validate(self):
        if self.hvac_device_config_volist:
            for k in self.hvac_device_config_volist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id
        result['hvacDeviceConfigVOList'] = []
        if self.hvac_device_config_volist is not None:
            for k in self.hvac_device_config_volist:
                result['hvacDeviceConfigVOList'].append(k.to_map() if k else None)
        if self.system_id is not None:
            result['systemId'] = self.system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')
        self.hvac_device_config_volist = []
        if m.get('hvacDeviceConfigVOList') is not None:
            for k in m.get('hvacDeviceConfigVOList'):
                temp_model = EditUnfavorableAreaDevicesRequestHvacDeviceConfigVOList()
                self.hvac_device_config_volist.append(temp_model.from_map(k))
        if m.get('systemId') is not None:
            self.system_id = m.get('systemId')
        return self


class EditUnfavorableAreaDevicesResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class EditUnfavorableAreaDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EditUnfavorableAreaDevicesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EditUnfavorableAreaDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateResultRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        product_id: int = None,
        product_type: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # The product id.
        # 
        # This parameter is required.
        self.product_id = product_id
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GenerateResultResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        # The returned data. `true` indicates that the request is successful, `false` indicates that the request fails.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GenerateResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAreaElecConstituteRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        year: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # Year.
        # 
        # This parameter is required.
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetAreaElecConstituteResponseBodyData(TeaModel):
    def __init__(
        self,
        light: List[CarbonEmissionElecSummaryItem] = None,
        nuclear: List[CarbonEmissionElecSummaryItem] = None,
        renewing: List[CarbonEmissionElecSummaryItem] = None,
        urban: List[CarbonEmissionElecSummaryItem] = None,
        water: List[CarbonEmissionElecSummaryItem] = None,
        wind: List[CarbonEmissionElecSummaryItem] = None,
        zero: List[CarbonEmissionElecSummaryItem] = None,
    ):
        # Photoelectric power consumption and carbon emission data of each enterprise.
        self.light = light
        # Data on nuclear power consumption and carbon emissions at each enterprise.
        self.nuclear = nuclear
        # Data on renewable electricity consumption and carbon emissions at each enterprise.
        self.renewing = renewing
        # Data on mains electricity consumption and carbon emission of each enterprise.
        self.urban = urban
        # Hydropower consumption and carbon emission data of each enterprise.
        self.water = water
        # Wind power consumption and carbon emission data of each enterprise.
        self.wind = wind
        # Data of zero electricity consumption and carbon emission of each enterprise.
        self.zero = zero

    def validate(self):
        if self.light:
            for k in self.light:
                if k:
                    k.validate()
        if self.nuclear:
            for k in self.nuclear:
                if k:
                    k.validate()
        if self.renewing:
            for k in self.renewing:
                if k:
                    k.validate()
        if self.urban:
            for k in self.urban:
                if k:
                    k.validate()
        if self.water:
            for k in self.water:
                if k:
                    k.validate()
        if self.wind:
            for k in self.wind:
                if k:
                    k.validate()
        if self.zero:
            for k in self.zero:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['light'] = []
        if self.light is not None:
            for k in self.light:
                result['light'].append(k.to_map() if k else None)
        result['nuclear'] = []
        if self.nuclear is not None:
            for k in self.nuclear:
                result['nuclear'].append(k.to_map() if k else None)
        result['renewing'] = []
        if self.renewing is not None:
            for k in self.renewing:
                result['renewing'].append(k.to_map() if k else None)
        result['urban'] = []
        if self.urban is not None:
            for k in self.urban:
                result['urban'].append(k.to_map() if k else None)
        result['water'] = []
        if self.water is not None:
            for k in self.water:
                result['water'].append(k.to_map() if k else None)
        result['wind'] = []
        if self.wind is not None:
            for k in self.wind:
                result['wind'].append(k.to_map() if k else None)
        result['zero'] = []
        if self.zero is not None:
            for k in self.zero:
                result['zero'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.light = []
        if m.get('light') is not None:
            for k in m.get('light'):
                temp_model = CarbonEmissionElecSummaryItem()
                self.light.append(temp_model.from_map(k))
        self.nuclear = []
        if m.get('nuclear') is not None:
            for k in m.get('nuclear'):
                temp_model = CarbonEmissionElecSummaryItem()
                self.nuclear.append(temp_model.from_map(k))
        self.renewing = []
        if m.get('renewing') is not None:
            for k in m.get('renewing'):
                temp_model = CarbonEmissionElecSummaryItem()
                self.renewing.append(temp_model.from_map(k))
        self.urban = []
        if m.get('urban') is not None:
            for k in m.get('urban'):
                temp_model = CarbonEmissionElecSummaryItem()
                self.urban.append(temp_model.from_map(k))
        self.water = []
        if m.get('water') is not None:
            for k in m.get('water'):
                temp_model = CarbonEmissionElecSummaryItem()
                self.water.append(temp_model.from_map(k))
        self.wind = []
        if m.get('wind') is not None:
            for k in m.get('wind'):
                temp_model = CarbonEmissionElecSummaryItem()
                self.wind.append(temp_model.from_map(k))
        self.zero = []
        if m.get('zero') is not None:
            for k in m.get('zero'):
                temp_model = CarbonEmissionElecSummaryItem()
                self.zero.append(temp_model.from_map(k))
        return self


class GetAreaElecConstituteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetAreaElecConstituteResponseBodyData = None,
        request_id: str = None,
    ):
        # The code returned for the request. A value of Success indicates that the request was successful. Other values indicate that the request failed. You can troubleshoot the error by viewing the error message returned.
        self.code = code
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetAreaElecConstituteResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetAreaElecConstituteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAreaElecConstituteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAreaElecConstituteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCarbonEmissionTrendRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        module_code: str = None,
        module_type: int = None,
        trend_type: int = None,
        year_list: List[int] = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # Module code.
        self.module_code = module_code
        # Module type.
        self.module_type = module_type
        # Trend Type.
        # 
        # This parameter is required.
        self.trend_type = trend_type
        # The list of inventory year.
        # 
        # This parameter is required.
        self.year_list = year_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.module_code is not None:
            result['moduleCode'] = self.module_code
        if self.module_type is not None:
            result['moduleType'] = self.module_type
        if self.trend_type is not None:
            result['trendType'] = self.trend_type
        if self.year_list is not None:
            result['yearList'] = self.year_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('moduleCode') is not None:
            self.module_code = m.get('moduleCode')
        if m.get('moduleType') is not None:
            self.module_type = m.get('moduleType')
        if m.get('trendType') is not None:
            self.trend_type = m.get('trendType')
        if m.get('yearList') is not None:
            self.year_list = m.get('yearList')
        return self


class GetCarbonEmissionTrendResponseBodyDataActualEmissionListItems(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        month: int = None,
        year: str = None,
    ):
        # Carbon emissions.
        self.carbon_emission_data = carbon_emission_data
        # The month.
        self.month = month
        # The year.
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetCarbonEmissionTrendResponseBodyDataActualEmissionList(TeaModel):
    def __init__(
        self,
        items: List[GetCarbonEmissionTrendResponseBodyDataActualEmissionListItems] = None,
        year: str = None,
    ):
        # Data item list.
        self.items = items
        # The year.
        self.year = year

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = GetCarbonEmissionTrendResponseBodyDataActualEmissionListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetCarbonEmissionTrendResponseBodyDataTargetEmissionListItems(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        month: int = None,
        year: str = None,
    ):
        # Carbon emissions.
        self.carbon_emission_data = carbon_emission_data
        # The month.
        self.month = month
        # The year.
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.month is not None:
            result['month'] = self.month
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetCarbonEmissionTrendResponseBodyDataTargetEmissionList(TeaModel):
    def __init__(
        self,
        items: List[GetCarbonEmissionTrendResponseBodyDataTargetEmissionListItems] = None,
        year: str = None,
    ):
        # Data item list.
        self.items = items
        # The year.
        self.year = year

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = GetCarbonEmissionTrendResponseBodyDataTargetEmissionListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetCarbonEmissionTrendResponseBodyData(TeaModel):
    def __init__(
        self,
        actual_emission_list: List[GetCarbonEmissionTrendResponseBodyDataActualEmissionList] = None,
        target_emission_list: List[GetCarbonEmissionTrendResponseBodyDataTargetEmissionList] = None,
    ):
        # Actual emission list.
        self.actual_emission_list = actual_emission_list
        # Target Emission List.
        self.target_emission_list = target_emission_list

    def validate(self):
        if self.actual_emission_list:
            for k in self.actual_emission_list:
                if k:
                    k.validate()
        if self.target_emission_list:
            for k in self.target_emission_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['actualEmissionList'] = []
        if self.actual_emission_list is not None:
            for k in self.actual_emission_list:
                result['actualEmissionList'].append(k.to_map() if k else None)
        result['targetEmissionList'] = []
        if self.target_emission_list is not None:
            for k in self.target_emission_list:
                result['targetEmissionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actual_emission_list = []
        if m.get('actualEmissionList') is not None:
            for k in m.get('actualEmissionList'):
                temp_model = GetCarbonEmissionTrendResponseBodyDataActualEmissionList()
                self.actual_emission_list.append(temp_model.from_map(k))
        self.target_emission_list = []
        if m.get('targetEmissionList') is not None:
            for k in m.get('targetEmissionList'):
                temp_model = GetCarbonEmissionTrendResponseBodyDataTargetEmissionList()
                self.target_emission_list.append(temp_model.from_map(k))
        return self


class GetCarbonEmissionTrendResponseBody(TeaModel):
    def __init__(
        self,
        data: GetCarbonEmissionTrendResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # Id of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetCarbonEmissionTrendResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetCarbonEmissionTrendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCarbonEmissionTrendResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCarbonEmissionTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatFolderListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ChatFolderItem] = None,
        request_id: str = None,
    ):
        # Returned data
        self.data = data
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ChatFolderItem()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetChatFolderListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChatFolderListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetChatFolderListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatListRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        session_id: str = None,
    ):
        # Pagination parameter, page number, starting from 1.
        self.current_page = current_page
        # Page size.
        self.page_size = page_size
        # Q&A session ID, used to record multiple Q&As for the same user.
        # 
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class GetChatListResponseBodyData(TeaModel):
    def __init__(
        self,
        chat_list: List[ChatItem] = None,
        current_page: int = None,
        page_size: int = None,
        total: int = None,
        total_page: int = None,
    ):
        # Q&A list.
        self.chat_list = chat_list
        # Current page number.
        self.current_page = current_page
        # Page size.
        self.page_size = page_size
        # Total number of records.
        self.total = total
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.chat_list:
            for k in self.chat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['chatList'] = []
        if self.chat_list is not None:
            for k in self.chat_list:
                result['chatList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        if self.total_page is not None:
            result['totalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chat_list = []
        if m.get('chatList') is not None:
            for k in m.get('chatList'):
                temp_model = ChatItem()
                self.chat_list.append(temp_model.from_map(k))
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')
        return self


class GetChatListResponseBody(TeaModel):
    def __init__(
        self,
        data: GetChatListResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned data structure.
        self.data = data
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetChatListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetChatListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChatListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetChatListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatSessionListRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        name: str = None,
        page_size: int = None,
        user_id: str = None,
    ):
        # Pagination parameter, page number, default is 1.
        self.current_page = current_page
        # Session name.
        self.name = name
        # Page size, default is 10.
        self.page_size = page_size
        # The unique identifier of the user. If not provided, the SDK calling account will be used as the user ID by default.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.name is not None:
            result['name'] = self.name
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetChatSessionListResponseBodyDataSessionList(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        folder_id: str = None,
        name: str = None,
        session_id: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        # Report creation timestamp, in milliseconds.
        self.create_time = create_time
        # Folder ID, used to specify the scope of documents to be queried.
        self.folder_id = folder_id
        # Session name
        self.name = name
        # Q&A session ID, used to record multiple Q&As of the same user.
        self.session_id = session_id
        # Modification time, in milliseconds.
        self.update_time = update_time
        # User ID of the current session.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        if self.name is not None:
            result['name'] = self.name
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetChatSessionListResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        session_list: List[GetChatSessionListResponseBodyDataSessionList] = None,
        total: int = None,
        total_page: int = None,
    ):
        # Current page number.
        self.current_page = current_page
        # 分页大小。
        self.page_size = page_size
        # Session list.
        self.session_list = session_list
        # Total number of records.
        self.total = total
        # Total number of pages
        self.total_page = total_page

    def validate(self):
        if self.session_list:
            for k in self.session_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['sessionList'] = []
        if self.session_list is not None:
            for k in self.session_list:
                result['sessionList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        if self.total_page is not None:
            result['totalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.session_list = []
        if m.get('sessionList') is not None:
            for k in m.get('sessionList'):
                temp_model = GetChatSessionListResponseBodyDataSessionList()
                self.session_list.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')
        return self


class GetChatSessionListResponseBody(TeaModel):
    def __init__(
        self,
        data: GetChatSessionListResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned data
        self.data = data
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetChatSessionListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetChatSessionListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChatSessionListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetChatSessionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataItemListRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class GetDataItemListResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        period: int = None,
        unit: str = None,
    ):
        # The identifier of the data item.
        self.code = code
        # The name of the data item.
        self.name = name
        # Data filling method, 1: monthly value 2: annual value.
        self.period = period
        # The data item unit.
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.name is not None:
            result['name'] = self.name
        if self.period is not None:
            result['period'] = self.period
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GetDataItemListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetDataItemListResponseBodyData] = None,
        request_id: str = None,
    ):
        # Response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetDataItemListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetDataItemListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataItemListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDataItemListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataQualityAnalysisRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        data_quality_evaluation_type: int = None,
        product_id: int = None,
        product_type: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # Data quality assessment type: 1 is DQI and 2 is DQR.
        # 
        # This parameter is required.
        self.data_quality_evaluation_type = data_quality_evaluation_type
        # The product id.
        # 
        # This parameter is required.
        self.product_id = product_id
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data_quality_evaluation_type is not None:
            result['dataQualityEvaluationType'] = self.data_quality_evaluation_type
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('dataQualityEvaluationType') is not None:
            self.data_quality_evaluation_type = m.get('dataQualityEvaluationType')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetDataQualityAnalysisResponseBodyDataDataQualityScore(TeaModel):
    def __init__(
        self,
        g_1: float = None,
        g_2: float = None,
        g_3: float = None,
        g_4: float = None,
    ):
        # Data quality evaluation indicator 1: activity data credibility.
        self.g_1 = g_1
        # Data quality evaluation indicator 2: data factor reliability.
        self.g_2 = g_2
        # Data quality evaluation indicator 3: time representativeness.
        self.g_3 = g_3
        # Data quality evaluation indicator 4: geographic representativeness.
        self.g_4 = g_4

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.g_1 is not None:
            result['g1'] = self.g_1
        if self.g_2 is not None:
            result['g2'] = self.g_2
        if self.g_3 is not None:
            result['g3'] = self.g_3
        if self.g_4 is not None:
            result['g4'] = self.g_4
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('g1') is not None:
            self.g_1 = m.get('g1')
        if m.get('g2') is not None:
            self.g_2 = m.get('g2')
        if m.get('g3') is not None:
            self.g_3 = m.get('g3')
        if m.get('g4') is not None:
            self.g_4 = m.get('g4')
        return self


class GetDataQualityAnalysisResponseBodyDataDataQuality(TeaModel):
    def __init__(
        self,
        inventory: str = None,
        score: GetDataQualityAnalysisResponseBodyDataDataQualityScore = None,
    ):
        # Inventory name
        self.inventory = inventory
        # Score. The distribution ranges from 1 to 5. A value closer to 1 indicates better data quality.
        self.score = score

    def validate(self):
        if self.score:
            self.score.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inventory is not None:
            result['inventory'] = self.inventory
        if self.score is not None:
            result['score'] = self.score.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inventory') is not None:
            self.inventory = m.get('inventory')
        if m.get('score') is not None:
            temp_model = GetDataQualityAnalysisResponseBodyDataDataQualityScore()
            self.score = temp_model.from_map(m['score'])
        return self


class GetDataQualityAnalysisResponseBodyDataDataQualityResult(TeaModel):
    def __init__(
        self,
        data_quality_score: float = None,
        g_1: float = None,
        g_2: float = None,
        g_3: float = None,
        g_4: float = None,
    ):
        # The score. This parameter is applicable to DQR results. The distribution ranges from 1 to 5. A value closer to 1 indicates better data quality. The number of valid digits is kept to four decimal places.
        self.data_quality_score = data_quality_score
        # Data quality evaluation indicator 1: activity data credibility.
        self.g_1 = g_1
        # Data quality evaluation indicator 2: data factor reliability.
        self.g_2 = g_2
        # Data quality evaluation indicator 3: time representativeness.
        self.g_3 = g_3
        # Data quality evaluation indicator 4: geographic representativeness.
        self.g_4 = g_4

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_quality_score is not None:
            result['data_quality_score'] = self.data_quality_score
        if self.g_1 is not None:
            result['g1'] = self.g_1
        if self.g_2 is not None:
            result['g2'] = self.g_2
        if self.g_3 is not None:
            result['g3'] = self.g_3
        if self.g_4 is not None:
            result['g4'] = self.g_4
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data_quality_score') is not None:
            self.data_quality_score = m.get('data_quality_score')
        if m.get('g1') is not None:
            self.g_1 = m.get('g1')
        if m.get('g2') is not None:
            self.g_2 = m.get('g2')
        if m.get('g3') is not None:
            self.g_3 = m.get('g3')
        if m.get('g4') is not None:
            self.g_4 = m.get('g4')
        return self


class GetDataQualityAnalysisResponseBodyDataSensitivityList(TeaModel):
    def __init__(
        self,
        id: str = None,
        inventory: str = None,
        reduction_list: List[str] = None,
        sensitivity: float = None,
    ):
        # Inventory id
        self.id = id
        # Name of the inventory item.
        self.inventory = inventory
        # List of emission reduction measures.
        self.reduction_list = reduction_list
        # Sensitivity percentage.
        self.sensitivity = sensitivity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.inventory is not None:
            result['inventory'] = self.inventory
        if self.reduction_list is not None:
            result['reductionList'] = self.reduction_list
        if self.sensitivity is not None:
            result['sensitivity'] = self.sensitivity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('inventory') is not None:
            self.inventory = m.get('inventory')
        if m.get('reductionList') is not None:
            self.reduction_list = m.get('reductionList')
        if m.get('sensitivity') is not None:
            self.sensitivity = m.get('sensitivity')
        return self


class GetDataQualityAnalysisResponseBodyDataUncertaintyValues(TeaModel):
    def __init__(
        self,
        inventory: str = None,
        uncertainty_contribution: str = None,
    ):
        # The name of the inventory. Format: process name / inventory name.
        self.inventory = inventory
        # Inventory uncertainty absolute contribution size. The impact of the quality of each inventory data on the carbon footprint results in the modeling process, when the uncertain contribution of a list is large, please improve its data quality as much as possible to improve the accuracy of carbon footprint analysis. The meaning of "1.4964" is not determined to contribute 1.4964 kgCO₂ e/unit, where unit is the unit of the product.
        self.uncertainty_contribution = uncertainty_contribution

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inventory is not None:
            result['inventory'] = self.inventory
        if self.uncertainty_contribution is not None:
            result['uncertaintyContribution'] = self.uncertainty_contribution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inventory') is not None:
            self.inventory = m.get('inventory')
        if m.get('uncertaintyContribution') is not None:
            self.uncertainty_contribution = m.get('uncertaintyContribution')
        return self


class GetDataQualityAnalysisResponseBodyData(TeaModel):
    def __init__(
        self,
        data_quality: List[GetDataQualityAnalysisResponseBodyDataDataQuality] = None,
        data_quality_result: GetDataQualityAnalysisResponseBodyDataDataQualityResult = None,
        sensitivity_list: List[GetDataQualityAnalysisResponseBodyDataSensitivityList] = None,
        uncertainty: str = None,
        uncertainty_values: List[GetDataQualityAnalysisResponseBodyDataUncertaintyValues] = None,
    ):
        # Score of each inventory.
        self.data_quality = data_quality
        # Data quality result.
        self.data_quality_result = data_quality_result
        # Sensitivity analysis list
        self.sensitivity_list = sensitivity_list
        # Uncertainty value. The model\\"s overall percentage uncertainty results. "10.00%" symbolizes a 10.00% uncertainty, indicating that the carbon footprint lies within ±10.00%. This is derived from a weighted aggregation of individual inventory uncertainties.
        self.uncertainty = uncertainty
        # Uncertainty list
        self.uncertainty_values = uncertainty_values

    def validate(self):
        if self.data_quality:
            for k in self.data_quality:
                if k:
                    k.validate()
        if self.data_quality_result:
            self.data_quality_result.validate()
        if self.sensitivity_list:
            for k in self.sensitivity_list:
                if k:
                    k.validate()
        if self.uncertainty_values:
            for k in self.uncertainty_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dataQuality'] = []
        if self.data_quality is not None:
            for k in self.data_quality:
                result['dataQuality'].append(k.to_map() if k else None)
        if self.data_quality_result is not None:
            result['dataQualityResult'] = self.data_quality_result.to_map()
        result['sensitivityList'] = []
        if self.sensitivity_list is not None:
            for k in self.sensitivity_list:
                result['sensitivityList'].append(k.to_map() if k else None)
        if self.uncertainty is not None:
            result['uncertainty'] = self.uncertainty
        result['uncertaintyValues'] = []
        if self.uncertainty_values is not None:
            for k in self.uncertainty_values:
                result['uncertaintyValues'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_quality = []
        if m.get('dataQuality') is not None:
            for k in m.get('dataQuality'):
                temp_model = GetDataQualityAnalysisResponseBodyDataDataQuality()
                self.data_quality.append(temp_model.from_map(k))
        if m.get('dataQualityResult') is not None:
            temp_model = GetDataQualityAnalysisResponseBodyDataDataQualityResult()
            self.data_quality_result = temp_model.from_map(m['dataQualityResult'])
        self.sensitivity_list = []
        if m.get('sensitivityList') is not None:
            for k in m.get('sensitivityList'):
                temp_model = GetDataQualityAnalysisResponseBodyDataSensitivityList()
                self.sensitivity_list.append(temp_model.from_map(k))
        if m.get('uncertainty') is not None:
            self.uncertainty = m.get('uncertainty')
        self.uncertainty_values = []
        if m.get('uncertaintyValues') is not None:
            for k in m.get('uncertaintyValues'):
                temp_model = GetDataQualityAnalysisResponseBodyDataUncertaintyValues()
                self.uncertainty_values.append(temp_model.from_map(k))
        return self


class GetDataQualityAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        data: GetDataQualityAnalysisResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetDataQualityAnalysisResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetDataQualityAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataQualityAnalysisResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDataQualityAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        ds: str = None,
        factory_id: str = None,
    ):
        # The ID of the device.
        # 
        # This parameter is required.
        self.device_id = device_id
        # The time string in the YYYY-mm-dd format.
        # 
        # This parameter is required.
        self.ds = ds
        # The ID of the site.
        # 
        # This parameter is required.
        self.factory_id = factory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.ds is not None:
            result['ds'] = self.ds
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('ds') is not None:
            self.ds = m.get('ds')
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')
        return self


class GetDeviceInfoResponseBodyDataRecordList(TeaModel):
    def __init__(
        self,
        identifier: str = None,
        param_name: str = None,
        statistics_date: str = None,
        type: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The device identifier.
        self.identifier = identifier
        # The parameter name.
        self.param_name = param_name
        # The date on which the statistics were collected.
        self.statistics_date = statistics_date
        # The type of the measuring point.
        self.type = type
        # The unit of the parameter value.
        self.unit = unit
        # The value of the measuring point.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.param_name is not None:
            result['paramName'] = self.param_name
        if self.statistics_date is not None:
            result['statisticsDate'] = self.statistics_date
        if self.type is not None:
            result['type'] = self.type
        if self.unit is not None:
            result['unit'] = self.unit
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('paramName') is not None:
            self.param_name = m.get('paramName')
        if m.get('statisticsDate') is not None:
            self.statistics_date = m.get('statisticsDate')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetDeviceInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        device_name: str = None,
        first_type_name: str = None,
        record_list: List[GetDeviceInfoResponseBodyDataRecordList] = None,
        second_type_name: str = None,
    ):
        # The ID of the device.
        self.device_id = device_id
        # The name of the device.
        self.device_name = device_name
        # The level 1 meter type.
        self.first_type_name = first_type_name
        # The device parameters.
        self.record_list = record_list
        # The level 2 meter type.
        self.second_type_name = second_type_name

    def validate(self):
        if self.record_list:
            for k in self.record_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.first_type_name is not None:
            result['firstTypeName'] = self.first_type_name
        result['recordList'] = []
        if self.record_list is not None:
            for k in self.record_list:
                result['recordList'].append(k.to_map() if k else None)
        if self.second_type_name is not None:
            result['secondTypeName'] = self.second_type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('firstTypeName') is not None:
            self.first_type_name = m.get('firstTypeName')
        self.record_list = []
        if m.get('recordList') is not None:
            for k in m.get('recordList'):
                temp_model = GetDeviceInfoResponseBodyDataRecordList()
                self.record_list.append(temp_model.from_map(k))
        if m.get('secondTypeName') is not None:
            self.second_type_name = m.get('secondTypeName')
        return self


class GetDeviceInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDeviceInfoResponseBodyData = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The code returned for the request. A value of Success indicates that the request was successful. Other values indicate that the request failed. You can troubleshoot the error by viewing the error message returned.
        self.code = code
        # The data returned.
        self.data = data
        # The HTTP status code.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetDeviceInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeviceInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceListRequest(TeaModel):
    def __init__(
        self,
        factory_id: str = None,
    ):
        # The ID of the site.
        # 
        # This parameter is required.
        self.factory_id = factory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')
        return self


class GetDeviceListResponseBodyDataDeviceListInfo(TeaModel):
    def __init__(
        self,
        const_kva: int = None,
        ct: int = None,
        magnification: int = None,
        pressure: int = None,
        pt: int = None,
    ):
        # The rated capacity.
        # Unit is kVA.
        self.const_kva = const_kva
        # The transformation ratio of current.
        self.ct = ct
        # The magnification ratio.
        self.magnification = magnification
        # The high and low voltage.
        self.pressure = pressure
        # The transformation ratio of voltage.
        self.pt = pt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.const_kva is not None:
            result['constKva'] = self.const_kva
        if self.ct is not None:
            result['ct'] = self.ct
        if self.magnification is not None:
            result['magnification'] = self.magnification
        if self.pressure is not None:
            result['pressure'] = self.pressure
        if self.pt is not None:
            result['pt'] = self.pt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('constKva') is not None:
            self.const_kva = m.get('constKva')
        if m.get('ct') is not None:
            self.ct = m.get('ct')
        if m.get('magnification') is not None:
            self.magnification = m.get('magnification')
        if m.get('pressure') is not None:
            self.pressure = m.get('pressure')
        if m.get('pt') is not None:
            self.pt = m.get('pt')
        return self


class GetDeviceListResponseBodyDataDeviceList(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        device_name: str = None,
        first_type_name: str = None,
        info: GetDeviceListResponseBodyDataDeviceListInfo = None,
        parent_device: str = None,
        second_type_name: str = None,
    ):
        # The device ID.
        self.device_id = device_id
        # The device name.
        self.device_name = device_name
        # The level 1 meter type.
        self.first_type_name = first_type_name
        # The device information.
        self.info = info
        # The ID of the parent device.
        self.parent_device = parent_device
        # The level 2 meter type.
        self.second_type_name = second_type_name

    def validate(self):
        if self.info:
            self.info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.first_type_name is not None:
            result['firstTypeName'] = self.first_type_name
        if self.info is not None:
            result['info'] = self.info.to_map()
        if self.parent_device is not None:
            result['parentDevice'] = self.parent_device
        if self.second_type_name is not None:
            result['secondTypeName'] = self.second_type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('firstTypeName') is not None:
            self.first_type_name = m.get('firstTypeName')
        if m.get('info') is not None:
            temp_model = GetDeviceListResponseBodyDataDeviceListInfo()
            self.info = temp_model.from_map(m['info'])
        if m.get('parentDevice') is not None:
            self.parent_device = m.get('parentDevice')
        if m.get('secondTypeName') is not None:
            self.second_type_name = m.get('secondTypeName')
        return self


class GetDeviceListResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        device_list: List[GetDeviceListResponseBodyDataDeviceList] = None,
        factory_id: str = None,
        http_code: int = None,
        success: bool = None,
    ):
        # The code returned for the request.
        self.code = code
        # The devices.
        self.device_list = device_list
        # The ID of the site.
        self.factory_id = factory_id
        # The HTTP status code.
        self.http_code = http_code
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.device_list:
            for k in self.device_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['deviceList'] = []
        if self.device_list is not None:
            for k in self.device_list:
                result['deviceList'].append(k.to_map() if k else None)
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.device_list = []
        if m.get('deviceList') is not None:
            for k in m.get('deviceList'):
                temp_model = GetDeviceListResponseBodyDataDeviceList()
                self.device_list.append(temp_model.from_map(k))
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetDeviceListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDeviceListResponseBodyData = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The data returned.
        self.data = data
        # The HTTP status code.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetDeviceListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetDeviceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeviceListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDeviceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocExtractionResultRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # - Task ID.
        # - taskId is obtained from the SubmitDocExtractionTaskAdvance and SubmitDocExtractionTask interfaces.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetDocExtractionResultResponseBodyDataKvListInfoContextConfidence(TeaModel):
    def __init__(
        self,
        key_confidence: float = None,
        value_confidence: float = None,
    ):
        # Key confidence level
        self.key_confidence = key_confidence
        # value confidence level
        self.value_confidence = value_confidence

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_confidence is not None:
            result['keyConfidence'] = self.key_confidence
        if self.value_confidence is not None:
            result['valueConfidence'] = self.value_confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyConfidence') is not None:
            self.key_confidence = m.get('keyConfidence')
        if m.get('valueConfidence') is not None:
            self.value_confidence = m.get('valueConfidence')
        return self


class GetDocExtractionResultResponseBodyDataKvListInfoContext(TeaModel):
    def __init__(
        self,
        confidence: GetDocExtractionResultResponseBodyDataKvListInfoContextConfidence = None,
        key: List[ContentItem] = None,
        value: List[ContentItem] = None,
    ):
        # Confidence level
        self.confidence = confidence
        # Details of key recall information
        self.key = key
        # Details of value recall information
        self.value = value

    def validate(self):
        if self.confidence:
            self.confidence.validate()
        if self.key:
            for k in self.key:
                if k:
                    k.validate()
        if self.value:
            for k in self.value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['confidence'] = self.confidence.to_map()
        result['key'] = []
        if self.key is not None:
            for k in self.key:
                result['key'].append(k.to_map() if k else None)
        result['value'] = []
        if self.value is not None:
            for k in self.value:
                result['value'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('confidence') is not None:
            temp_model = GetDocExtractionResultResponseBodyDataKvListInfoContextConfidence()
            self.confidence = temp_model.from_map(m['confidence'])
        self.key = []
        if m.get('key') is not None:
            for k in m.get('key'):
                temp_model = ContentItem()
                self.key.append(temp_model.from_map(k))
        self.value = []
        if m.get('value') is not None:
            for k in m.get('value'):
                temp_model = ContentItem()
                self.value.append(temp_model.from_map(k))
        return self


class GetDocExtractionResultResponseBodyDataKvListInfo(TeaModel):
    def __init__(
        self,
        context: GetDocExtractionResultResponseBodyDataKvListInfoContext = None,
        key_name: str = None,
        key_value: str = None,
    ):
        # Recalled content
        self.context = context
        # Field key name
        self.key_name = key_name
        # Field key value
        self.key_value = key_value

    def validate(self):
        if self.context:
            self.context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['context'] = self.context.to_map()
        if self.key_name is not None:
            result['keyName'] = self.key_name
        if self.key_value is not None:
            result['keyValue'] = self.key_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('context') is not None:
            temp_model = GetDocExtractionResultResponseBodyDataKvListInfoContext()
            self.context = temp_model.from_map(m['context'])
        if m.get('keyName') is not None:
            self.key_name = m.get('keyName')
        if m.get('keyValue') is not None:
            self.key_value = m.get('keyValue')
        return self


class GetDocExtractionResultResponseBodyData(TeaModel):
    def __init__(
        self,
        kv_list_info: List[GetDocExtractionResultResponseBodyDataKvListInfo] = None,
    ):
        # Details of document extraction results
        self.kv_list_info = kv_list_info

    def validate(self):
        if self.kv_list_info:
            for k in self.kv_list_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['kvListInfo'] = []
        if self.kv_list_info is not None:
            for k in self.kv_list_info:
                result['kvListInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kv_list_info = []
        if m.get('kvListInfo') is not None:
            for k in m.get('kvListInfo'):
                temp_model = GetDocExtractionResultResponseBodyDataKvListInfo()
                self.kv_list_info.append(temp_model.from_map(k))
        return self


class GetDocExtractionResultResponseBody(TeaModel):
    def __init__(
        self,
        data: GetDocExtractionResultResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned data structure.
        self.data = data
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetDocExtractionResultResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetDocExtractionResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocExtractionResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDocExtractionResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocParsingResultRequest(TeaModel):
    def __init__(
        self,
        return_format: str = None,
        task_id: str = None,
    ):
        # - The document parsing result supports two formats: markdown and json.
        # - By default, the result is returned in markdown format.
        self.return_format = return_format
        # - Task ID.
        # - The taskId is obtained from the SubmitDocParsingTaskAdvance or SubmitDocParsingTask interfaces.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_format is not None:
            result['returnFormat'] = self.return_format
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnFormat') is not None:
            self.return_format = m.get('returnFormat')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetDocParsingResultResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        # - The parsed content of the document.
        # - The format (markdown or json) is determined by the returnFormat parameter. For specific format details, refer to: [json return structure](https://www.alibabacloud.com/help/en/energy-expert/developer-reference/interface-attached-information#b644b6255cojj)
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class GetDocParsingResultResponseBody(TeaModel):
    def __init__(
        self,
        data: GetDocParsingResultResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned result.
        self.data = data
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetDocParsingResultResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetDocParsingResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocParsingResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDocParsingResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocumentAnalyzeResultRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # Job ID, specifying which document\\"s parsing result to query. This is a return parameter from the \\"Submit Document Parsing Job\\" interface.
        # 
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['jobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        return self


class GetDocumentAnalyzeResultResponseBodyDataKvListInfoContextConfidence(TeaModel):
    def __init__(
        self,
        key_confidence: float = None,
        value_confidence: float = None,
    ):
        # Confidence of Key
        self.key_confidence = key_confidence
        # Confidence of Value
        self.value_confidence = value_confidence

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_confidence is not None:
            result['keyConfidence'] = self.key_confidence
        if self.value_confidence is not None:
            result['valueConfidence'] = self.value_confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyConfidence') is not None:
            self.key_confidence = m.get('keyConfidence')
        if m.get('valueConfidence') is not None:
            self.value_confidence = m.get('valueConfidence')
        return self


class GetDocumentAnalyzeResultResponseBodyDataKvListInfoContext(TeaModel):
    def __init__(
        self,
        confidence: GetDocumentAnalyzeResultResponseBodyDataKvListInfoContextConfidence = None,
        key: List[ContentItem] = None,
        value: List[ContentItem] = None,
    ):
        # Confidence
        self.confidence = confidence
        # Key Recall Information
        self.key = key
        # Value Recall Information
        self.value = value

    def validate(self):
        if self.confidence:
            self.confidence.validate()
        if self.key:
            for k in self.key:
                if k:
                    k.validate()
        if self.value:
            for k in self.value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['confidence'] = self.confidence.to_map()
        result['key'] = []
        if self.key is not None:
            for k in self.key:
                result['key'].append(k.to_map() if k else None)
        result['value'] = []
        if self.value is not None:
            for k in self.value:
                result['value'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('confidence') is not None:
            temp_model = GetDocumentAnalyzeResultResponseBodyDataKvListInfoContextConfidence()
            self.confidence = temp_model.from_map(m['confidence'])
        self.key = []
        if m.get('key') is not None:
            for k in m.get('key'):
                temp_model = ContentItem()
                self.key.append(temp_model.from_map(k))
        self.value = []
        if m.get('value') is not None:
            for k in m.get('value'):
                temp_model = ContentItem()
                self.value.append(temp_model.from_map(k))
        return self


class GetDocumentAnalyzeResultResponseBodyDataKvListInfo(TeaModel):
    def __init__(
        self,
        context: GetDocumentAnalyzeResultResponseBodyDataKvListInfoContext = None,
        key_name: str = None,
        key_value: str = None,
    ):
        # Recalled Content
        self.context = context
        # Field Key Name
        self.key_name = key_name
        # Field Key Value
        self.key_value = key_value

    def validate(self):
        if self.context:
            self.context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['context'] = self.context.to_map()
        if self.key_name is not None:
            result['keyName'] = self.key_name
        if self.key_value is not None:
            result['keyValue'] = self.key_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('context') is not None:
            temp_model = GetDocumentAnalyzeResultResponseBodyDataKvListInfoContext()
            self.context = temp_model.from_map(m['context'])
        if m.get('keyName') is not None:
            self.key_name = m.get('keyName')
        if m.get('keyValue') is not None:
            self.key_value = m.get('keyValue')
        return self


class GetDocumentAnalyzeResultResponseBodyData(TeaModel):
    def __init__(
        self,
        kv_list_info: List[GetDocumentAnalyzeResultResponseBodyDataKvListInfo] = None,
    ):
        # Document Parsing Result
        self.kv_list_info = kv_list_info

    def validate(self):
        if self.kv_list_info:
            for k in self.kv_list_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['kvListInfo'] = []
        if self.kv_list_info is not None:
            for k in self.kv_list_info:
                result['kvListInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kv_list_info = []
        if m.get('kvListInfo') is not None:
            for k in m.get('kvListInfo'):
                temp_model = GetDocumentAnalyzeResultResponseBodyDataKvListInfo()
                self.kv_list_info.append(temp_model.from_map(k))
        return self


class GetDocumentAnalyzeResultResponseBody(TeaModel):
    def __init__(
        self,
        data: GetDocumentAnalyzeResultResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned Data
        self.data = data
        # Request ID
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetDocumentAnalyzeResultResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetDocumentAnalyzeResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocumentAnalyzeResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDocumentAnalyzeResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetElecConstituteRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        year: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # Year.
        # 
        # This parameter is required.
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetElecConstituteResponseBodyDataLight(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
    ):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data
        # The unit.
        self.data_unit = data_unit
        # The name.
        self.name = name
        # The unique identifier of name.
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        return self


class GetElecConstituteResponseBodyDataNuclear(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
    ):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data
        # The unit.
        self.data_unit = data_unit
        # The name.
        self.name = name
        # The unique identifier of name.
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        return self


class GetElecConstituteResponseBodyDataRenewing(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
    ):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data
        # The unit.
        self.data_unit = data_unit
        # The name.
        self.name = name
        # The unique identifier of name.
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        return self


class GetElecConstituteResponseBodyDataUrban(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
    ):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data
        # The unit.
        self.data_unit = data_unit
        # The name.
        self.name = name
        # The unique identifier of name.
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        return self


class GetElecConstituteResponseBodyDataWater(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
    ):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data
        # The unit.
        self.data_unit = data_unit
        # The name.
        self.name = name
        # The unique identifier of name.
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        return self


class GetElecConstituteResponseBodyDataWind(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
    ):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data
        # The unit.
        self.data_unit = data_unit
        # The name.
        self.name = name
        # The unique identifier of name.
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        return self


class GetElecConstituteResponseBodyDataZero(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
    ):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data
        # The unit.
        self.data_unit = data_unit
        # The name.
        self.name = name
        # The unique identifier of name.
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        return self


class GetElecConstituteResponseBodyData(TeaModel):
    def __init__(
        self,
        light: GetElecConstituteResponseBodyDataLight = None,
        nuclear: GetElecConstituteResponseBodyDataNuclear = None,
        renewing: GetElecConstituteResponseBodyDataRenewing = None,
        urban: GetElecConstituteResponseBodyDataUrban = None,
        water: GetElecConstituteResponseBodyDataWater = None,
        wind: GetElecConstituteResponseBodyDataWind = None,
        zero: GetElecConstituteResponseBodyDataZero = None,
    ):
        # Photoelectric power consumption and carbon emission data of each enterprise.
        self.light = light
        # Data on nuclear power consumption and carbon emissions at each enterprise.
        self.nuclear = nuclear
        # Data on renewable electricity consumption and carbon emissions at each enterprise.
        self.renewing = renewing
        # Data on mains power electricity consumption and carbon emission of each enterprise.
        self.urban = urban
        # Hydropower consumption and carbon emission data of each enterprise.
        self.water = water
        # Wind power consumption and carbon emission data of each enterprise.
        self.wind = wind
        # Data of zero electricity consumption and carbon emission of each enterprise.
        self.zero = zero

    def validate(self):
        if self.light:
            self.light.validate()
        if self.nuclear:
            self.nuclear.validate()
        if self.renewing:
            self.renewing.validate()
        if self.urban:
            self.urban.validate()
        if self.water:
            self.water.validate()
        if self.wind:
            self.wind.validate()
        if self.zero:
            self.zero.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.light is not None:
            result['light'] = self.light.to_map()
        if self.nuclear is not None:
            result['nuclear'] = self.nuclear.to_map()
        if self.renewing is not None:
            result['renewing'] = self.renewing.to_map()
        if self.urban is not None:
            result['urban'] = self.urban.to_map()
        if self.water is not None:
            result['water'] = self.water.to_map()
        if self.wind is not None:
            result['wind'] = self.wind.to_map()
        if self.zero is not None:
            result['zero'] = self.zero.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('light') is not None:
            temp_model = GetElecConstituteResponseBodyDataLight()
            self.light = temp_model.from_map(m['light'])
        if m.get('nuclear') is not None:
            temp_model = GetElecConstituteResponseBodyDataNuclear()
            self.nuclear = temp_model.from_map(m['nuclear'])
        if m.get('renewing') is not None:
            temp_model = GetElecConstituteResponseBodyDataRenewing()
            self.renewing = temp_model.from_map(m['renewing'])
        if m.get('urban') is not None:
            temp_model = GetElecConstituteResponseBodyDataUrban()
            self.urban = temp_model.from_map(m['urban'])
        if m.get('water') is not None:
            temp_model = GetElecConstituteResponseBodyDataWater()
            self.water = temp_model.from_map(m['water'])
        if m.get('wind') is not None:
            temp_model = GetElecConstituteResponseBodyDataWind()
            self.wind = temp_model.from_map(m['wind'])
        if m.get('zero') is not None:
            temp_model = GetElecConstituteResponseBodyDataZero()
            self.zero = temp_model.from_map(m['zero'])
        return self


class GetElecConstituteResponseBody(TeaModel):
    def __init__(
        self,
        data: GetElecConstituteResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # Id of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetElecConstituteResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetElecConstituteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetElecConstituteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetElecConstituteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetElecTrendRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        year_list: List[int] = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # List of years.
        # 
        # This parameter is required.
        self.year_list = year_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.year_list is not None:
            result['yearList'] = self.year_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('yearList') is not None:
            self.year_list = m.get('yearList')
        return self


class GetElecTrendResponseBodyDataLight(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        month: int = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
        year: str = None,
    ):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data
        # The unit.
        self.data_unit = data_unit
        # Month
        self.month = month
        # Power type name.
        self.name = name
        # Power Type Code
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e. 50%).
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data
        # Year
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.month is not None:
            result['month'] = self.month
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetElecTrendResponseBodyDataNuclear(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        month: int = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
        year: str = None,
    ):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data
        # The price unit.
        self.data_unit = data_unit
        # Month
        self.month = month
        # Power Type Name
        self.name = name
        # Power Type Code
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data
        # Year
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.month is not None:
            result['month'] = self.month
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetElecTrendResponseBodyDataRenewing(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        month: int = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
        year: str = None,
    ):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data
        # The price unit.
        self.data_unit = data_unit
        # Month
        self.month = month
        # Power Type Name
        self.name = name
        # Power Type Code
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data
        # Year
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.month is not None:
            result['month'] = self.month
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetElecTrendResponseBodyDataUrban(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        month: int = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
        year: str = None,
    ):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data
        # The price unit.
        self.data_unit = data_unit
        # Month
        self.month = month
        # Power Type Name
        self.name = name
        # Power Type Code
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e. 50%).
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data
        # Year
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.month is not None:
            result['month'] = self.month
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetElecTrendResponseBodyDataWater(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        month: int = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
        year: str = None,
    ):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data
        # The unit.
        self.data_unit = data_unit
        # Month
        self.month = month
        # Power Type Name
        self.name = name
        # Power Type Code
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e. 50%).
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data
        # Year
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.month is not None:
            result['month'] = self.month
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetElecTrendResponseBodyDataWind(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        month: int = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
        year: str = None,
    ):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data
        # The price unit.
        self.data_unit = data_unit
        # Month
        self.month = month
        # Power Type Name
        self.name = name
        # Power Type Code
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data
        # Year
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.month is not None:
            result['month'] = self.month
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetElecTrendResponseBodyDataZero(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        month: int = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
        year: str = None,
    ):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data
        # The price unit.
        self.data_unit = data_unit
        # Month
        self.month = month
        # Power Type Name
        self.name = name
        # Power Type Code
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data
        # Year
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.month is not None:
            result['month'] = self.month
        if self.name is not None:
            result['name'] = self.name
        if self.name_key is not None:
            result['nameKey'] = self.name_key
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.raw_data is not None:
            result['rawData'] = self.raw_data
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetElecTrendResponseBodyData(TeaModel):
    def __init__(
        self,
        light: List[GetElecTrendResponseBodyDataLight] = None,
        nuclear: List[GetElecTrendResponseBodyDataNuclear] = None,
        renewing: List[GetElecTrendResponseBodyDataRenewing] = None,
        urban: List[GetElecTrendResponseBodyDataUrban] = None,
        water: List[GetElecTrendResponseBodyDataWater] = None,
        wind: List[GetElecTrendResponseBodyDataWind] = None,
        zero: List[GetElecTrendResponseBodyDataZero] = None,
    ):
        # Photoelectricity monthly electricity consumption and carbon emissions and other data.
        self.light = light
        # Monthly electricity consumption and carbon emissions data for nuclear power
        self.nuclear = nuclear
        # Monthly data on renewable electricity consumption and carbon emissions
        self.renewing = renewing
        # Data such as monthly electricity consumption and carbon emissions from the mains.
        self.urban = urban
        # Monthly data on electricity consumption and carbon emissions for hydropower.
        self.water = water
        # Monthly wind power consumption and carbon emission data
        self.wind = wind
        # Zero electricity monthly electricity consumption and carbon emissions and other data.
        self.zero = zero

    def validate(self):
        if self.light:
            for k in self.light:
                if k:
                    k.validate()
        if self.nuclear:
            for k in self.nuclear:
                if k:
                    k.validate()
        if self.renewing:
            for k in self.renewing:
                if k:
                    k.validate()
        if self.urban:
            for k in self.urban:
                if k:
                    k.validate()
        if self.water:
            for k in self.water:
                if k:
                    k.validate()
        if self.wind:
            for k in self.wind:
                if k:
                    k.validate()
        if self.zero:
            for k in self.zero:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['light'] = []
        if self.light is not None:
            for k in self.light:
                result['light'].append(k.to_map() if k else None)
        result['nuclear'] = []
        if self.nuclear is not None:
            for k in self.nuclear:
                result['nuclear'].append(k.to_map() if k else None)
        result['renewing'] = []
        if self.renewing is not None:
            for k in self.renewing:
                result['renewing'].append(k.to_map() if k else None)
        result['urban'] = []
        if self.urban is not None:
            for k in self.urban:
                result['urban'].append(k.to_map() if k else None)
        result['water'] = []
        if self.water is not None:
            for k in self.water:
                result['water'].append(k.to_map() if k else None)
        result['wind'] = []
        if self.wind is not None:
            for k in self.wind:
                result['wind'].append(k.to_map() if k else None)
        result['zero'] = []
        if self.zero is not None:
            for k in self.zero:
                result['zero'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.light = []
        if m.get('light') is not None:
            for k in m.get('light'):
                temp_model = GetElecTrendResponseBodyDataLight()
                self.light.append(temp_model.from_map(k))
        self.nuclear = []
        if m.get('nuclear') is not None:
            for k in m.get('nuclear'):
                temp_model = GetElecTrendResponseBodyDataNuclear()
                self.nuclear.append(temp_model.from_map(k))
        self.renewing = []
        if m.get('renewing') is not None:
            for k in m.get('renewing'):
                temp_model = GetElecTrendResponseBodyDataRenewing()
                self.renewing.append(temp_model.from_map(k))
        self.urban = []
        if m.get('urban') is not None:
            for k in m.get('urban'):
                temp_model = GetElecTrendResponseBodyDataUrban()
                self.urban.append(temp_model.from_map(k))
        self.water = []
        if m.get('water') is not None:
            for k in m.get('water'):
                temp_model = GetElecTrendResponseBodyDataWater()
                self.water.append(temp_model.from_map(k))
        self.wind = []
        if m.get('wind') is not None:
            for k in m.get('wind'):
                temp_model = GetElecTrendResponseBodyDataWind()
                self.wind.append(temp_model.from_map(k))
        self.zero = []
        if m.get('zero') is not None:
            for k in m.get('zero'):
                temp_model = GetElecTrendResponseBodyDataZero()
                self.zero.append(temp_model.from_map(k))
        return self


class GetElecTrendResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetElecTrendResponseBodyData = None,
        request_id: str = None,
    ):
        # The code returned for the request. A value of Success indicates that the request was successful. Other values indicate that the request failed. You can troubleshoot the error by viewing the error message returned.
        self.code = code
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetElecTrendResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetElecTrendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetElecTrendResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetElecTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEmissionSourceConstituteRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        module_code: str = None,
        module_type: int = None,
        year: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # Module code.
        self.module_code = module_code
        # Module type.
        # 
        # This parameter is required.
        self.module_type = module_type
        # Year of inventory.
        # 
        # This parameter is required.
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.module_code is not None:
            result['moduleCode'] = self.module_code
        if self.module_type is not None:
            result['moduleType'] = self.module_type
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('moduleCode') is not None:
            self.module_code = m.get('moduleCode')
        if m.get('moduleType') is not None:
            self.module_type = m.get('moduleType')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetEmissionSourceConstituteResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ConstituteItem] = None,
        request_id: str = None,
    ):
        # Response parameters
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ConstituteItem()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetEmissionSourceConstituteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEmissionSourceConstituteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEmissionSourceConstituteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEmissionSummaryRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        module_code: str = None,
        module_type: int = None,
        year: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # Module code.
        self.module_code = module_code
        # Module type.
        self.module_type = module_type
        # Year of inventory.
        # 
        # This parameter is required.
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.module_code is not None:
            result['moduleCode'] = self.module_code
        if self.module_type is not None:
            result['moduleType'] = self.module_type
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('moduleCode') is not None:
            self.module_code = m.get('moduleCode')
        if m.get('moduleType') is not None:
            self.module_type = m.get('moduleType')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetEmissionSummaryResponseBodyData(TeaModel):
    def __init__(
        self,
        actual_emission_ratio: float = None,
        carbon_save_conversion: float = None,
        current_period_carbon_emission_data: float = None,
        is_weighting: bool = None,
        last_period_carbon_emission_data: float = None,
        last_period_weighting_carbon_emission_data: float = None,
        ratio: float = None,
        total_carbon_emission_data: float = None,
        weighting_carbon_emission_data: float = None,
        weighting_ratio: float = None,
    ):
        # Percentage of scheduled.
        self.actual_emission_ratio = actual_emission_ratio
        # Carbon emissions reduction.
        self.carbon_save_conversion = carbon_save_conversion
        # Statistical indicators for this cycle.
        self.current_period_carbon_emission_data = current_period_carbon_emission_data
        # Whether to show the weighting ratio carbon emission.
        self.is_weighting = is_weighting
        # Last period statistical indicators.
        self.last_period_carbon_emission_data = last_period_carbon_emission_data
        # Calculation of carbon emissions based on shareholding ratio in the last cycle.
        self.last_period_weighting_carbon_emission_data = last_period_weighting_carbon_emission_data
        # Year-on-year.
        self.ratio = ratio
        # Total carbon emissions.
        self.total_carbon_emission_data = total_carbon_emission_data
        # Calculate carbon emissions by share ratio
        self.weighting_carbon_emission_data = weighting_carbon_emission_data
        # Year-on-year of weighting ratio carbon emissions.
        self.weighting_ratio = weighting_ratio

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_emission_ratio is not None:
            result['actualEmissionRatio'] = self.actual_emission_ratio
        if self.carbon_save_conversion is not None:
            result['carbonSaveConversion'] = self.carbon_save_conversion
        if self.current_period_carbon_emission_data is not None:
            result['currentPeriodCarbonEmissionData'] = self.current_period_carbon_emission_data
        if self.is_weighting is not None:
            result['isWeighting'] = self.is_weighting
        if self.last_period_carbon_emission_data is not None:
            result['lastPeriodCarbonEmissionData'] = self.last_period_carbon_emission_data
        if self.last_period_weighting_carbon_emission_data is not None:
            result['lastPeriodWeightingCarbonEmissionData'] = self.last_period_weighting_carbon_emission_data
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.total_carbon_emission_data is not None:
            result['totalCarbonEmissionData'] = self.total_carbon_emission_data
        if self.weighting_carbon_emission_data is not None:
            result['weightingCarbonEmissionData'] = self.weighting_carbon_emission_data
        if self.weighting_ratio is not None:
            result['weightingRatio'] = self.weighting_ratio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actualEmissionRatio') is not None:
            self.actual_emission_ratio = m.get('actualEmissionRatio')
        if m.get('carbonSaveConversion') is not None:
            self.carbon_save_conversion = m.get('carbonSaveConversion')
        if m.get('currentPeriodCarbonEmissionData') is not None:
            self.current_period_carbon_emission_data = m.get('currentPeriodCarbonEmissionData')
        if m.get('isWeighting') is not None:
            self.is_weighting = m.get('isWeighting')
        if m.get('lastPeriodCarbonEmissionData') is not None:
            self.last_period_carbon_emission_data = m.get('lastPeriodCarbonEmissionData')
        if m.get('lastPeriodWeightingCarbonEmissionData') is not None:
            self.last_period_weighting_carbon_emission_data = m.get('lastPeriodWeightingCarbonEmissionData')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('totalCarbonEmissionData') is not None:
            self.total_carbon_emission_data = m.get('totalCarbonEmissionData')
        if m.get('weightingCarbonEmissionData') is not None:
            self.weighting_carbon_emission_data = m.get('weightingCarbonEmissionData')
        if m.get('weightingRatio') is not None:
            self.weighting_ratio = m.get('weightingRatio')
        return self


class GetEmissionSummaryResponseBody(TeaModel):
    def __init__(
        self,
        data: GetEmissionSummaryResponseBodyData = None,
        request_id: str = None,
    ):
        # Details of summarized data
        self.data = data
        # Id of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetEmissionSummaryResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetEmissionSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEmissionSummaryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEmissionSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEpdInventoryConstituteRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        product_id: int = None,
        product_type: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # The product id.
        # 
        # This parameter is required.
        self.product_id = product_id
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetEpdInventoryConstituteResponseBody(TeaModel):
    def __init__(
        self,
        data: List[EpdInventoryConstituteItem] = None,
        request_id: str = None,
    ):
        # List of environmental impact results.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = EpdInventoryConstituteItem()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetEpdInventoryConstituteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEpdInventoryConstituteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEpdInventoryConstituteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEpdSummaryRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        product_id: int = None,
        product_type: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # The product id.
        # 
        # This parameter is required.
        self.product_id = product_id
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetEpdSummaryResponseBodyData(TeaModel):
    def __init__(
        self,
        carbon_emission: float = None,
        indicator: str = None,
        key: str = None,
        method: str = None,
        name: str = None,
        num: int = None,
        pre_unit: str = None,
        state: int = None,
    ):
        # Emissions. The result is maintained up to 31 decimal places for precise intermediate calculation and subsequently truncated for display. It is advised to pair the emissions figure with the unit of the environmental impact result for a comprehensive understanding.
        self.carbon_emission = carbon_emission
        # The evaluation index adopted for the environmental impact
        self.indicator = indicator
        # The category key. The environmental impact category. Currently, a maximum of 19 categories are supported. Enumeration refers to [Carbon Footprint Appendices](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/CarbonFootprintAppendices-en.pdf).
        self.key = key
        # Calculation method standard
        self.method = method
        # The name of the category.
        self.name = name
        # Category num: the unique serial number of the environmental impact category. A maximum of 19 categories are supported. Enumeration refers to [Carbon Footprint Appendices](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/CarbonFootprintAppendices-en.pdf).
        self.num = num
        # Environmental impact result Value Unit.
        self.pre_unit = pre_unit
        # The data status. 1 indicates that the calculation is accurate, 2 indicates that the default data is used, and 3 indicates that the missing factor uses the value of 0.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission
        if self.indicator is not None:
            result['indicator'] = self.indicator
        if self.key is not None:
            result['key'] = self.key
        if self.method is not None:
            result['method'] = self.method
        if self.name is not None:
            result['name'] = self.name
        if self.num is not None:
            result['num'] = self.num
        if self.pre_unit is not None:
            result['preUnit'] = self.pre_unit
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')
        if m.get('indicator') is not None:
            self.indicator = m.get('indicator')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('num') is not None:
            self.num = m.get('num')
        if m.get('preUnit') is not None:
            self.pre_unit = m.get('preUnit')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class GetEpdSummaryResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetEpdSummaryResponseBodyData] = None,
        request_id: str = None,
    ):
        # Response parameters
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetEpdSummaryResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetEpdSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEpdSummaryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEpdSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFootprintListRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        page_size: int = None,
        product_type: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # The pagination parameter. The number of the page that starts from 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The number of entries returned on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetFootprintListResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        amount: float = None,
        auth_status: int = None,
        check_end_time: str = None,
        check_start_time: str = None,
        code: str = None,
        created_by: str = None,
        id: int = None,
        is_demo_model: int = None,
        life_cycle: str = None,
        life_cycle_type: int = None,
        name: str = None,
        type: str = None,
        unit: str = None,
    ):
        # The amount of the product.
        self.amount = amount
        # Authentication status enumeration value, please refer to [link](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/CarbonFootprintAppendices-en.pdf).
        self.auth_status = auth_status
        # Calculation end time.
        self.check_end_time = check_end_time
        # Calculation start time.
        self.check_start_time = check_start_time
        # The enterprise code.
        self.code = code
        # The user who created it.
        self.created_by = created_by
        # The product ID.
        self.id = id
        # Indicates whether the demo model is a built-in model. A value of 1 indicates a true value and a value of 0 indicates a false value.
        self.is_demo_model = is_demo_model
        # The literal expression corresponding to lifeCycleType, `From Cradle to Gate` and `From Cradle to Grave`.
        self.life_cycle = life_cycle
        # 1 is `From Cradle to Gate`, and 2 is `From Cradle to Grave`.
        self.life_cycle_type = life_cycle_type
        # The product name.
        self.name = name
        # Product category enumeration value, please refer to [Carbon Footprint Appendices](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/CarbonFootprintAppendices-en.pdf).
        self.type = type
        # Unit enumeration value. Please refer to [Carbon Footprint Appendices](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/CarbonFootprintAppendices-en.pdf).
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.auth_status is not None:
            result['authStatus'] = self.auth_status
        if self.check_end_time is not None:
            result['checkEndTime'] = self.check_end_time
        if self.check_start_time is not None:
            result['checkStartTime'] = self.check_start_time
        if self.code is not None:
            result['code'] = self.code
        if self.created_by is not None:
            result['createdBy'] = self.created_by
        if self.id is not None:
            result['id'] = self.id
        if self.is_demo_model is not None:
            result['isDemoModel'] = self.is_demo_model
        if self.life_cycle is not None:
            result['lifeCycle'] = self.life_cycle
        if self.life_cycle_type is not None:
            result['lifeCycleType'] = self.life_cycle_type
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('authStatus') is not None:
            self.auth_status = m.get('authStatus')
        if m.get('checkEndTime') is not None:
            self.check_end_time = m.get('checkEndTime')
        if m.get('checkStartTime') is not None:
            self.check_start_time = m.get('checkStartTime')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isDemoModel') is not None:
            self.is_demo_model = m.get('isDemoModel')
        if m.get('lifeCycle') is not None:
            self.life_cycle = m.get('lifeCycle')
        if m.get('lifeCycleType') is not None:
            self.life_cycle_type = m.get('lifeCycleType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GetFootprintListResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        records: List[GetFootprintListResponseBodyDataRecords] = None,
        total: int = None,
        total_page: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The number of entries returned on each page.
        self.page_size = page_size
        # Product Detail List.
        self.records = records
        # The total number of entries returned.
        self.total = total
        # Total Pages
        self.total_page = total_page

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        if self.total_page is not None:
            result['totalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = GetFootprintListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')
        return self


class GetFootprintListResponseBody(TeaModel):
    def __init__(
        self,
        data: GetFootprintListResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetFootprintListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetFootprintListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFootprintListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFootprintListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGasConstituteRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        module_code: str = None,
        module_type: int = None,
        year: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # Module code.
        self.module_code = module_code
        # Module type.
        # 
        # This parameter is required.
        self.module_type = module_type
        # Year
        # 
        # This parameter is required.
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.module_code is not None:
            result['moduleCode'] = self.module_code
        if self.module_type is not None:
            result['moduleType'] = self.module_type
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('moduleCode') is not None:
            self.module_code = m.get('moduleCode')
        if m.get('moduleType') is not None:
            self.module_type = m.get('moduleType')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetGasConstituteResponseBodyData(TeaModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        gas_emission_data: float = None,
        name: str = None,
        ratio: float = None,
        type: int = None,
    ):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data
        # Gas emissions
        self.gas_emission_data = gas_emission_data
        # Name of gas
        self.name = name
        # Proportion of carbon emissions. Example value: 0.5 (50%)
        self.ratio = ratio
        # Gas Type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data
        if self.gas_emission_data is not None:
            result['gasEmissionData'] = self.gas_emission_data
        if self.name is not None:
            result['name'] = self.name
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')
        if m.get('gasEmissionData') is not None:
            self.gas_emission_data = m.get('gasEmissionData')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetGasConstituteResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetGasConstituteResponseBodyData] = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetGasConstituteResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetGasConstituteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGasConstituteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGasConstituteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGwpBenchmarkListRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        product_id: int = None,
        product_type: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # The product id.
        # 
        # This parameter is required.
        self.product_id = product_id
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetGwpBenchmarkListResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        active_reduction: float = None,
        benchmark_emission: float = None,
        benchmark_name: str = None,
        carbon_emission: float = None,
        name: str = None,
        percent: str = None,
    ):
        # `activeReduction=benchmarkEmission-carbonEmission` Generally, baseline emissions are greater than inventory emissions. Maintain four decimal places. Unit pertains to a higher-level unit.
        self.active_reduction = active_reduction
        # Benchmark emissions. Maintain four decimal places. Unit pertains to a higher-level unit.
        self.benchmark_emission = benchmark_emission
        # Benchmark name
        self.benchmark_name = benchmark_name
        # Inventory emissions. Maintain four decimal places. Unit pertains to a higher-level unit.
        self.carbon_emission = carbon_emission
        # name
        self.name = name
        # Unused temporarily.
        self.percent = percent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_reduction is not None:
            result['activeReduction'] = self.active_reduction
        if self.benchmark_emission is not None:
            result['benchmarkEmission'] = self.benchmark_emission
        if self.benchmark_name is not None:
            result['benchmarkName'] = self.benchmark_name
        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission
        if self.name is not None:
            result['name'] = self.name
        if self.percent is not None:
            result['percent'] = self.percent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeReduction') is not None:
            self.active_reduction = m.get('activeReduction')
        if m.get('benchmarkEmission') is not None:
            self.benchmark_emission = m.get('benchmarkEmission')
        if m.get('benchmarkName') is not None:
            self.benchmark_name = m.get('benchmarkName')
        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        return self


class GetGwpBenchmarkListResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[GetGwpBenchmarkListResponseBodyDataItems] = None,
        unit: str = None,
    ):
        # Active carbon reduction ranking list.
        self.items = items
        # unit of emissions. The default value is `kgCO₂e/productUnit`. 
        # The `productUnit` is the unit selected for the product. The unit value is changed to `tCO₂e/productUnit` or `gCO₂e/productUnit`. For more information, see the remarks in the quantity column.
        self.unit = unit

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = GetGwpBenchmarkListResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GetGwpBenchmarkListResponseBody(TeaModel):
    def __init__(
        self,
        data: GetGwpBenchmarkListResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetGwpBenchmarkListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetGwpBenchmarkListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGwpBenchmarkListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGwpBenchmarkListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGwpBenchmarkSummaryRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        product_id: int = None,
        product_type: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # The product id.
        # 
        # This parameter is required.
        self.product_id = product_id
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetGwpBenchmarkSummaryResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        name: str = None,
        percent: str = None,
        quantity: int = None,
        unit: str = None,
    ):
        # Name of carbon reduction details.
        self.name = name
        # Percentage of emissions. The value is of the string type. Two decimal places are reserved for numbers. For example, "99.01" indicates the 99.01% of this type of emissions to the total emissions. Note that the returned string itself does not contain a percent sign.
        self.percent = percent
        # Emission amount is presented with four decimal places. Normally, modeling doesn\\"t result in negative values, but users can represent carbon reductions as negatives. The amount, paired with the unit, defines the emissions. Both are dynamically adjusted. If emissions exceed `1000 kgCO₂e/productUnit`, they convert to `tCO₂e/productUnit`. If they fall below `1 kgCO₂e/productUnit`, they convert to `gCO₂e/productUnit`. Otherwise, they stay in `kgCO₂e/productUnit`.
        self.quantity = quantity
        # Unit of emissions. The default value is `kgCO₂e/productUnit.` `productUnit` is the unit selected for the product. The unit value is changed to `tCO₂e/productUnit` or `gCO₂e/productUnit`. For more information, see the remarks in the quantity column.
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.percent is not None:
            result['percent'] = self.percent
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GetGwpBenchmarkSummaryResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[GetGwpBenchmarkSummaryResponseBodyDataItems] = None,
        quantity: int = None,
        unit: str = None,
    ):
        # Carbon Reduction Contribution Top4 Details.
        self.items = items
        # Emission amount is presented with four decimal places. Normally, modeling doesn\\"t result in negative values, but users can represent carbon reductions as negatives. The amount, paired with the unit, defines the emissions. Both are dynamically adjusted. If emissions exceed `1000 kgCO₂e/productUnit`, they convert to `tCO₂e/productUnit`. If they fall below `1 kgCO₂e/productUnit`, they convert to `gCO₂e/productUnit`. Otherwise, they stay in `kgCO₂e/productUnit`.
        self.quantity = quantity
        # Unit of emissions. The default value is `kgCO₂e/productUnit.` `productUnit` is the unit selected for the product. The unit value is changed to `tCO₂e/productUnit` or `gCO₂e/productUnit`. For more information, see the remarks in the quantity column.
        self.unit = unit

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = GetGwpBenchmarkSummaryResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GetGwpBenchmarkSummaryResponseBody(TeaModel):
    def __init__(
        self,
        data: GetGwpBenchmarkSummaryResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetGwpBenchmarkSummaryResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetGwpBenchmarkSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGwpBenchmarkSummaryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGwpBenchmarkSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGwpInventoryConstituteRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        product_id: int = None,
        product_type: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # The product id.
        # 
        # This parameter is required.
        self.product_id = product_id
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetGwpInventoryConstituteResponseBodyData(TeaModel):
    def __init__(
        self,
        by_resource_type: List[GwpInventoryConstitute] = None,
        carbon_emission: float = None,
        items: List[GwpInventoryConstitute] = None,
        name: str = None,
        unit: str = None,
    ):
        # Aggregated by resource type of an inventory.
        self.by_resource_type = by_resource_type
        # Emission quantity: may be positive, negative, or 0. To ensure the calculation accuracy, 24 decimal places are reserved for the calculation process. We recommend that you intercept data based on your business requirements.
        self.carbon_emission = carbon_emission
        # Organized by hierarchy from high to low, according to the flow-> process-> inventory hierarchy.
        self.items = items
        # The name.
        self.name = name
        # Emission Unit.
        self.unit = unit

    def validate(self):
        if self.by_resource_type:
            for k in self.by_resource_type:
                if k:
                    k.validate()
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['byResourceType'] = []
        if self.by_resource_type is not None:
            for k in self.by_resource_type:
                result['byResourceType'].append(k.to_map() if k else None)
        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.by_resource_type = []
        if m.get('byResourceType') is not None:
            for k in m.get('byResourceType'):
                temp_model = GwpInventoryConstitute()
                self.by_resource_type.append(temp_model.from_map(k))
        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = GwpInventoryConstitute()
                self.items.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GetGwpInventoryConstituteResponseBody(TeaModel):
    def __init__(
        self,
        data: GetGwpInventoryConstituteResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetGwpInventoryConstituteResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetGwpInventoryConstituteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGwpInventoryConstituteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGwpInventoryConstituteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGwpInventorySummaryRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        product_id: int = None,
        product_type: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # The product id.
        # 
        # This parameter is required.
        self.product_id = product_id
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetGwpInventorySummaryResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        name: str = None,
        percent: str = None,
        quantity: float = None,
        unit: str = None,
    ):
        # Inventory resource type name.
        self.name = name
        # Percentage.
        self.percent = percent
        # Quantity.
        self.quantity = quantity
        # The unit.
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.percent is not None:
            result['percent'] = self.percent
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GetGwpInventorySummaryResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[GetGwpInventorySummaryResponseBodyDataItems] = None,
        quantity: float = None,
        result_generate_time: int = None,
        unit: str = None,
    ):
        # Top 4 types of carbon footprint contribution.
        self.items = items
        # The emission quantity.
        self.quantity = quantity
        # The time when the result was generated, in the millisecond timestamp format.
        self.result_generate_time = result_generate_time
        # Emission Unit.
        self.unit = unit

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.result_generate_time is not None:
            result['resultGenerateTime'] = self.result_generate_time
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = GetGwpInventorySummaryResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('resultGenerateTime') is not None:
            self.result_generate_time = m.get('resultGenerateTime')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GetGwpInventorySummaryResponseBody(TeaModel):
    def __init__(
        self,
        data: GetGwpInventorySummaryResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned results.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetGwpInventorySummaryResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetGwpInventorySummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGwpInventorySummaryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGwpInventorySummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInventoryListRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        emission_type: str = None,
        group: str = None,
        method_type: str = None,
        product_id: int = None,
        product_type: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # Type of emission
        # 
        # >  Valid values: footprint | emission. Meaning: footprint: all inventories are involved in the calculation; emission: only inventories with positive and zero emissions are involved in the calculation, and negative numbers are not involved in the calculation.
        # 
        # This parameter is required.
        self.emission_type = emission_type
        # Group by
        # 
        # >  Valid values: resource | process | resourceType | processType. Meaning: resource: aggregation by inventory group, process: aggregation by operation group, resourceType: aggregation by inventory type, processType: aggregation by phase group
        # 
        # This parameter is required.
        self.group = group
        # The type of the obtained environmental impact: gwp indicates the carbon footprint of climate change. 
        # <props="intl">[For more information, see the environment impact category enumeration.](https://www.alibabacloud.com/help/en/energy-expert/developer-reference/enumerated-values-of-energy-expert#RhGn7)
        # 
        # This parameter is required.
        self.method_type = method_type
        # The product id.
        # 
        # This parameter is required.
        self.product_id = product_id
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.emission_type is not None:
            result['emissionType'] = self.emission_type
        if self.group is not None:
            result['group'] = self.group
        if self.method_type is not None:
            result['methodType'] = self.method_type
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('emissionType') is not None:
            self.emission_type = m.get('emissionType')
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('methodType') is not None:
            self.method_type = m.get('methodType')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetInventoryListResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        carbon_emission: float = None,
        name: str = None,
        percent: str = None,
        process_name: str = None,
    ):
        # Emission quantity: may be positive, negative, or 0. To ensure the calculation accuracy, 24 decimal places are reserved for the calculation process. We recommend that you intercept data based on your business requirements.
        self.carbon_emission = carbon_emission
        # Name 
        # 
        # > The name is related to the request parameters group. Request parameters: resource, return name parameter meaning: list name; request parameters: process, return name parameter meaning: process name; request parameters: resourceType, return name parameter meaning: inventory resource type name; request parameters: processType, return name parameter meaning: flow name.
        self.name = name
        # Percentage
        self.percent = percent
        # Process Name: It is only meaningful when the request parameters group is resource.
        self.process_name = process_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission
        if self.name is not None:
            result['name'] = self.name
        if self.percent is not None:
            result['percent'] = self.percent
        if self.process_name is not None:
            result['processName'] = self.process_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('percent') is not None:
            self.percent = m.get('percent')
        if m.get('processName') is not None:
            self.process_name = m.get('processName')
        return self


class GetInventoryListResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[GetInventoryListResponseBodyDataItems] = None,
        product_unit: str = None,
        unit: str = None,
    ):
        # Inventory detail.
        self.items = items
        # Unit of product.
        self.product_unit = product_unit
        # Emission Unit: The default value is kgCO₂ /productUnit. productUnit is the unit selected for the product. The unit value is changed to tCO₂ e/productUnit or gCO₂ e/productUnit based on the emission quantity. For more information, see the quantity column.
        self.unit = unit

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.product_unit is not None:
            result['productUnit'] = self.product_unit
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = GetInventoryListResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('productUnit') is not None:
            self.product_unit = m.get('productUnit')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class GetInventoryListResponseBody(TeaModel):
    def __init__(
        self,
        data: GetInventoryListResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetInventoryListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetInventoryListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInventoryListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetInventoryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrgAndFactoryResponseBodyDataFactoryList(TeaModel):
    def __init__(
        self,
        factory_id: str = None,
        factory_name: str = None,
    ):
        # The site ID.
        self.factory_id = factory_id
        # The site name.
        self.factory_name = factory_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id
        if self.factory_name is not None:
            result['factoryName'] = self.factory_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')
        if m.get('factoryName') is not None:
            self.factory_name = m.get('factoryName')
        return self


class GetOrgAndFactoryResponseBodyData(TeaModel):
    def __init__(
        self,
        aliyun_pk: str = None,
        factory_list: List[GetOrgAndFactoryResponseBodyDataFactoryList] = None,
        organization_id: str = None,
        organization_name: str = None,
    ):
        # The Alibaba Cloud account ID.
        self.aliyun_pk = aliyun_pk
        # The sites.
        self.factory_list = factory_list
        # The enterprise ID.
        self.organization_id = organization_id
        # The enterprise name.
        self.organization_name = organization_name

    def validate(self):
        if self.factory_list:
            for k in self.factory_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_pk is not None:
            result['aliyunPk'] = self.aliyun_pk
        result['factoryList'] = []
        if self.factory_list is not None:
            for k in self.factory_list:
                result['factoryList'].append(k.to_map() if k else None)
        if self.organization_id is not None:
            result['organizationId'] = self.organization_id
        if self.organization_name is not None:
            result['organizationName'] = self.organization_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunPk') is not None:
            self.aliyun_pk = m.get('aliyunPk')
        self.factory_list = []
        if m.get('factoryList') is not None:
            for k in m.get('factoryList'):
                temp_model = GetOrgAndFactoryResponseBodyDataFactoryList()
                self.factory_list.append(temp_model.from_map(k))
        if m.get('organizationId') is not None:
            self.organization_id = m.get('organizationId')
        if m.get('organizationName') is not None:
            self.organization_name = m.get('organizationName')
        return self


class GetOrgAndFactoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOrgAndFactoryResponseBodyData] = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The code returned for the request.
        self.code = code
        # data
        self.data = data
        # The HTTP status code.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetOrgAndFactoryResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetOrgAndFactoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOrgAndFactoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetOrgAndFactoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrgConstituteRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        module_code: str = None,
        module_type: int = None,
        year: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # Module code.
        self.module_code = module_code
        # Module type.
        # 
        # This parameter is required.
        self.module_type = module_type
        # Year.
        # 
        # This parameter is required.
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.module_code is not None:
            result['moduleCode'] = self.module_code
        if self.module_type is not None:
            result['moduleType'] = self.module_type
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('moduleCode') is not None:
            self.module_code = m.get('moduleCode')
        if m.get('moduleType') is not None:
            self.module_type = m.get('moduleType')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class GetOrgConstituteResponseBody(TeaModel):
    def __init__(
        self,
        data: OrgEmission = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = OrgEmission()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetOrgConstituteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOrgConstituteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetOrgConstituteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPcrInfoRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        product_id: str = None,
        product_type: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # The product id.
        # 
        # This parameter is required.
        self.product_id = product_id
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetPcrInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        name: str = None,
        url: str = None,
    ):
        # The timestamp when the report was created. The timestamp is in milliseconds.
        self.create_time = create_time
        # Report name
        self.name = name
        # Download url link.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.name is not None:
            result['name'] = self.name
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetPcrInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: GetPcrInfoResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetPcrInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetPcrInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPcrInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPcrInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetReductionProposalRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        data_quality_evaluation_type: int = None,
        product_id: int = None,
        product_type: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # The type of the data quality evaluation. 1 is DQI and 2 is DQR.
        # 
        # This parameter is required.
        self.data_quality_evaluation_type = data_quality_evaluation_type
        # The product id.
        # 
        # This parameter is required.
        self.product_id = product_id
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data_quality_evaluation_type is not None:
            result['dataQualityEvaluationType'] = self.data_quality_evaluation_type
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('dataQualityEvaluationType') is not None:
            self.data_quality_evaluation_type = m.get('dataQualityEvaluationType')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class GetReductionProposalResponseBodyData(TeaModel):
    def __init__(
        self,
        reduction: str = None,
        reduction_evaluation: str = None,
    ):
        # Proactive carbon reduction recommendations and advice.
        self.reduction = reduction
        # Active carbon reduction assessment.
        self.reduction_evaluation = reduction_evaluation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reduction is not None:
            result['reduction'] = self.reduction
        if self.reduction_evaluation is not None:
            result['reductionEvaluation'] = self.reduction_evaluation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reduction') is not None:
            self.reduction = m.get('reduction')
        if m.get('reductionEvaluation') is not None:
            self.reduction_evaluation = m.get('reductionEvaluation')
        return self


class GetReductionProposalResponseBody(TeaModel):
    def __init__(
        self,
        data: GetReductionProposalResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetReductionProposalResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetReductionProposalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetReductionProposalResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetReductionProposalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVLExtractionResultRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # - taskID.
        # 
        # - The taskId is obtained from the interfaces SubmitVLExtractionTaskAdvance and SubmitVLExtractionTask.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetVLExtractionResultResponseBodyDataKvListInfoContextConfidence(TeaModel):
    def __init__(
        self,
        key_confidence: float = None,
        value_confidence: float = None,
    ):
        # Confidence of Key
        self.key_confidence = key_confidence
        # Confidence of Value
        self.value_confidence = value_confidence

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_confidence is not None:
            result['keyConfidence'] = self.key_confidence
        if self.value_confidence is not None:
            result['valueConfidence'] = self.value_confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyConfidence') is not None:
            self.key_confidence = m.get('keyConfidence')
        if m.get('valueConfidence') is not None:
            self.value_confidence = m.get('valueConfidence')
        return self


class GetVLExtractionResultResponseBodyDataKvListInfoContext(TeaModel):
    def __init__(
        self,
        confidence: GetVLExtractionResultResponseBodyDataKvListInfoContextConfidence = None,
        key: List[ContentItem] = None,
        value: List[ContentItem] = None,
    ):
        # Confidence
        self.confidence = confidence
        # Key recall information details
        self.key = key
        # Value Recall Information
        self.value = value

    def validate(self):
        if self.confidence:
            self.confidence.validate()
        if self.key:
            for k in self.key:
                if k:
                    k.validate()
        if self.value:
            for k in self.value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['confidence'] = self.confidence.to_map()
        result['key'] = []
        if self.key is not None:
            for k in self.key:
                result['key'].append(k.to_map() if k else None)
        result['value'] = []
        if self.value is not None:
            for k in self.value:
                result['value'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('confidence') is not None:
            temp_model = GetVLExtractionResultResponseBodyDataKvListInfoContextConfidence()
            self.confidence = temp_model.from_map(m['confidence'])
        self.key = []
        if m.get('key') is not None:
            for k in m.get('key'):
                temp_model = ContentItem()
                self.key.append(temp_model.from_map(k))
        self.value = []
        if m.get('value') is not None:
            for k in m.get('value'):
                temp_model = ContentItem()
                self.value.append(temp_model.from_map(k))
        return self


class GetVLExtractionResultResponseBodyDataKvListInfo(TeaModel):
    def __init__(
        self,
        context: GetVLExtractionResultResponseBodyDataKvListInfoContext = None,
        key_name: str = None,
        key_value: str = None,
    ):
        # Recall content
        self.context = context
        # Field Key name
        self.key_name = key_name
        # Field key value
        self.key_value = key_value

    def validate(self):
        if self.context:
            self.context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['context'] = self.context.to_map()
        if self.key_name is not None:
            result['keyName'] = self.key_name
        if self.key_value is not None:
            result['keyValue'] = self.key_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('context') is not None:
            temp_model = GetVLExtractionResultResponseBodyDataKvListInfoContext()
            self.context = temp_model.from_map(m['context'])
        if m.get('keyName') is not None:
            self.key_name = m.get('keyName')
        if m.get('keyValue') is not None:
            self.key_value = m.get('keyValue')
        return self


class GetVLExtractionResultResponseBodyData(TeaModel):
    def __init__(
        self,
        kv_list_info: List[GetVLExtractionResultResponseBodyDataKvListInfo] = None,
    ):
        # Document Parsing Result
        self.kv_list_info = kv_list_info

    def validate(self):
        if self.kv_list_info:
            for k in self.kv_list_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['kvListInfo'] = []
        if self.kv_list_info is not None:
            for k in self.kv_list_info:
                result['kvListInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kv_list_info = []
        if m.get('kvListInfo') is not None:
            for k in m.get('kvListInfo'):
                temp_model = GetVLExtractionResultResponseBodyDataKvListInfo()
                self.kv_list_info.append(temp_model.from_map(k))
        return self


class GetVLExtractionResultResponseBody(TeaModel):
    def __init__(
        self,
        data: GetVLExtractionResultResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned Data
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetVLExtractionResultResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetVLExtractionResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVLExtractionResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetVLExtractionResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IsCompletedRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        product_id: int = None,
        product_type: int = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # The product id.
        # 
        # This parameter is required.
        self.product_id = product_id
        # Product type: 1 indicates that the carbon footprint of the product is requested, and 5 indicates that the carbon footprint of the supply chain is requested.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        return self


class IsCompletedResponseBodyData(TeaModel):
    def __init__(
        self,
        modified_time: int = None,
        task_key: str = None,
        task_short_result: str = None,
        task_status: str = None,
    ):
        # Modified time in milliseconds, e.g. 1711438780000.
        self.modified_time = modified_time
        # The unique key of this generation task.
        self.task_key = task_key
        # Unused temporarily.
        self.task_short_result = task_short_result
        # The status of the report generation task. The possible values are `running`, `success`, and `error`, which mean generating, generating succeeded, and generating failed, respectively. If you encounter a result generation failure, check the model, correct the model, and then generate the result again.
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time
        if self.task_key is not None:
            result['taskKey'] = self.task_key
        if self.task_short_result is not None:
            result['taskShortResult'] = self.task_short_result
        if self.task_status is not None:
            result['taskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')
        if m.get('taskKey') is not None:
            self.task_key = m.get('taskKey')
        if m.get('taskShortResult') is not None:
            self.task_short_result = m.get('taskShortResult')
        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')
        return self


class IsCompletedResponseBody(TeaModel):
    def __init__(
        self,
        data: IsCompletedResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = IsCompletedResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class IsCompletedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IsCompletedResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IsCompletedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushDeviceDataRequestDevices(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        device_id: str = None,
        record_time: str = None,
    ):
        # Measuring point information To avoid accuracy problems, the measurement point data is uniformly transmitted to the string. The function of missing required fields cannot be used normally. Some functions may be affected due to the lack of recommend fields. For details, please refer to the notes of equipment measuring points in the appendix. [Reference Point Definition](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/Deviceappendixes-en.pdf
        # )
        # 
        # This parameter is required.
        self.data = data
        # If the deviceType parameter is set to 12, 13, or 17, you must set the system_id parameter. The field name is still device_id. If the deviceType parameter is set to 15 or 16, no Other situations will be transmitted.
        # 
        # This parameter is required.
        self.device_id = device_id
        # Data generation time of measuring point.
        # 
        # This parameter is required.
        self.record_time = record_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.record_time is not None:
            result['recordTime'] = self.record_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('recordTime') is not None:
            self.record_time = m.get('recordTime')
        return self


class PushDeviceDataRequest(TeaModel):
    def __init__(
        self,
        device_type: str = None,
        devices: List[PushDeviceDataRequestDevices] = None,
    ):
        # The type of the device. [View device type definitions](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/Deviceappendixes-en.pdf)
        # 
        # This parameter is required.
        self.device_type = device_type
        # List of devices to which data is pushed.
        # 
        # This parameter is required.
        self.devices = devices

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_type is not None:
            result['deviceType'] = self.device_type
        result['devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['devices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceType') is not None:
            self.device_type = m.get('deviceType')
        self.devices = []
        if m.get('devices') is not None:
            for k in m.get('devices'):
                temp_model = PushDeviceDataRequestDevices()
                self.devices.append(temp_model.from_map(k))
        return self


class PushDeviceDataResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # Whether the data is pushed successfully. Success is returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class PushDeviceDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushDeviceDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PushDeviceDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushItemDataRequestItems(TeaModel):
    def __init__(
        self,
        code: str = None,
        month: str = None,
        value: float = None,
    ):
        # API data identification.<props="intl">For details: [GetDataItemList ](https://www.alibabacloud.com/help/en/energy-expert/developer-reference/api-energyexpertexternal-2022-09-23-getdataitemlist)
        # 
        # This parameter is required.
        self.code = code
        # The month.
        # 
        # This parameter is required.
        self.month = month
        # The value of the data item.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.month is not None:
            result['month'] = self.month
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('month') is not None:
            self.month = m.get('month')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class PushItemDataRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        items: PushItemDataRequestItems = None,
        year: str = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # List of data to be pushed.
        # 
        # This parameter is required.
        self.items = items
        # The year of the data created.
        # 
        # This parameter is required.
        self.year = year

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.items is not None:
            result['items'] = self.items.to_map()
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('items') is not None:
            temp_model = PushItemDataRequestItems()
            self.items = temp_model.from_map(m['items'])
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class PushItemDataResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        # Whether the data is pushed successfully.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class PushItemDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushItemDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PushItemDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecalculateCarbonEmissionRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        year: str = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # Year of inventory.
        # 
        # This parameter is required.
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.year is not None:
            result['year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('year') is not None:
            self.year = m.get('year')
        return self


class RecalculateCarbonEmissionResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        # The returned data. A value of true indicates that the request is successful. A value of false indicates that the request fails.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RecalculateCarbonEmissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecalculateCarbonEmissionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecalculateCarbonEmissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendDocumentAskQuestionRequest(TeaModel):
    def __init__(
        self,
        folder_id: str = None,
        prompt: str = None,
        session_id: str = None,
    ):
        # Folder ID, used to specify the range of documents for the query. If it is empty, it indicates that all documents under the default folder will be queried.
        self.folder_id = folder_id
        # The question queried by the user
        # 
        # This parameter is required.
        self.prompt = prompt
        # Q&A session ID, used to record multiple Q&A interactions of the same user. If it is empty, it indicates that sessions are not distinguished.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        if self.prompt is not None:
            result['prompt'] = self.prompt
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class SendDocumentAskQuestionResponseBodyData(TeaModel):
    def __init__(
        self,
        answer: str = None,
        document: List[str] = None,
    ):
        # Q&A result
        self.answer = answer
        # Documents associated with the answer returned by the query
        self.document = document

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['answer'] = self.answer
        if self.document is not None:
            result['document'] = self.document
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answer') is not None:
            self.answer = m.get('answer')
        if m.get('document') is not None:
            self.document = m.get('document')
        return self


class SendDocumentAskQuestionResponseBody(TeaModel):
    def __init__(
        self,
        data: SendDocumentAskQuestionResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned data
        self.data = data
        # Request ID
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = SendDocumentAskQuestionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class SendDocumentAskQuestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendDocumentAskQuestionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendDocumentAskQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetRunningPlanRequest(TeaModel):
    def __init__(
        self,
        control_type: int = None,
        date_type: int = None,
        earliest_startup_time: str = None,
        end_time: str = None,
        factory_id: str = None,
        latest_shutdown_time: str = None,
        max_carbon_dioxide: float = None,
        max_tem: float = None,
        min_tem: float = None,
        p_key: str = None,
        season_mode: int = None,
        start_time: str = None,
        statistics_time: str = None,
        system_id: str = None,
        working_end_time: str = None,
        working_start_time: str = None,
    ):
        self.control_type = control_type
        self.date_type = date_type
        self.earliest_startup_time = earliest_startup_time
        self.end_time = end_time
        # This parameter is required.
        self.factory_id = factory_id
        self.latest_shutdown_time = latest_shutdown_time
        self.max_carbon_dioxide = max_carbon_dioxide
        self.max_tem = max_tem
        self.min_tem = min_tem
        self.p_key = p_key
        self.season_mode = season_mode
        self.start_time = start_time
        self.statistics_time = statistics_time
        # This parameter is required.
        self.system_id = system_id
        self.working_end_time = working_end_time
        self.working_start_time = working_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_type is not None:
            result['controlType'] = self.control_type
        if self.date_type is not None:
            result['dateType'] = self.date_type
        if self.earliest_startup_time is not None:
            result['earliestStartupTime'] = self.earliest_startup_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id
        if self.latest_shutdown_time is not None:
            result['latestShutdownTime'] = self.latest_shutdown_time
        if self.max_carbon_dioxide is not None:
            result['maxCarbonDioxide'] = self.max_carbon_dioxide
        if self.max_tem is not None:
            result['maxTem'] = self.max_tem
        if self.min_tem is not None:
            result['minTem'] = self.min_tem
        if self.p_key is not None:
            result['pKey'] = self.p_key
        if self.season_mode is not None:
            result['seasonMode'] = self.season_mode
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.statistics_time is not None:
            result['statisticsTime'] = self.statistics_time
        if self.system_id is not None:
            result['systemId'] = self.system_id
        if self.working_end_time is not None:
            result['workingEndTime'] = self.working_end_time
        if self.working_start_time is not None:
            result['workingStartTime'] = self.working_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('controlType') is not None:
            self.control_type = m.get('controlType')
        if m.get('dateType') is not None:
            self.date_type = m.get('dateType')
        if m.get('earliestStartupTime') is not None:
            self.earliest_startup_time = m.get('earliestStartupTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')
        if m.get('latestShutdownTime') is not None:
            self.latest_shutdown_time = m.get('latestShutdownTime')
        if m.get('maxCarbonDioxide') is not None:
            self.max_carbon_dioxide = m.get('maxCarbonDioxide')
        if m.get('maxTem') is not None:
            self.max_tem = m.get('maxTem')
        if m.get('minTem') is not None:
            self.min_tem = m.get('minTem')
        if m.get('pKey') is not None:
            self.p_key = m.get('pKey')
        if m.get('seasonMode') is not None:
            self.season_mode = m.get('seasonMode')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('statisticsTime') is not None:
            self.statistics_time = m.get('statisticsTime')
        if m.get('systemId') is not None:
            self.system_id = m.get('systemId')
        if m.get('workingEndTime') is not None:
            self.working_end_time = m.get('workingEndTime')
        if m.get('workingStartTime') is not None:
            self.working_start_time = m.get('workingStartTime')
        return self


class SetRunningPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class SetRunningPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetRunningPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetRunningPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDocExtractionTaskRequest(TeaModel):
    def __init__(
        self,
        extract_type: str = None,
        file_name: str = None,
        file_url: str = None,
        folder_id: str = None,
        template_id: str = None,
    ):
        # Document extraction type:
        # Supports rag and long text understanding types, default is rag.
        self.extract_type = extract_type
        # The filename must include the file type extension.
        # 
        # This parameter is required.
        self.file_name = file_name
        # Choose one of fileUrl or fileUrlObject:
        # 
        # - fileUrl: Use by providing the document URL, for a single document (supports up to 1000 pages, 100MB in size)
        # 
        # - fileUrlObject: Use when calling the interface with local file upload, for a single document (supports up to 1000 pages, 100 MB in size)
        # 
        # > The relationship between file extraction methods and supported document types
        # > - Long text RAG: Supports pdf, doc/docx, xlsx, csv, txt, up to 1000 pages
        # > - Image processing: Supports pdf, jpg, jpeg, png, bmp, jpe, tif, tiff, webp, heic
        # > - Long text understanding: Supports doc/docx, xlsx, pdf, csv, txt
        self.file_url = file_url
        # - A unique knowledge base folder ID, used when you need to categorize documents and control the scope of documents for online Q&A queries.
        # - The folder ID needs to be obtained by logging into the intelligent document console.
        self.folder_id = folder_id
        # A unique extraction template ID used to specify the content to be extracted from the document. You need to log in to the template management page to configure the template and obtain the corresponding template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extract_type is not None:
            result['extractType'] = self.extract_type
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_url is not None:
            result['fileUrl'] = self.file_url
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extractType') is not None:
            self.extract_type = m.get('extractType')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class SubmitDocExtractionTaskAdvanceRequest(TeaModel):
    def __init__(
        self,
        extract_type: str = None,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        folder_id: str = None,
        template_id: str = None,
    ):
        # Document extraction type:
        # Supports rag and long text understanding types, default is rag.
        self.extract_type = extract_type
        # The filename must include the file type extension.
        # 
        # This parameter is required.
        self.file_name = file_name
        # Choose one of fileUrl or fileUrlObject:
        # 
        # - fileUrl: Use by providing the document URL, for a single document (supports up to 1000 pages, 100MB in size)
        # 
        # - fileUrlObject: Use when calling the interface with local file upload, for a single document (supports up to 1000 pages, 100 MB in size)
        # 
        # > The relationship between file extraction methods and supported document types
        # > - Long text RAG: Supports pdf, doc/docx, xlsx, csv, txt, up to 1000 pages
        # > - Image processing: Supports pdf, jpg, jpeg, png, bmp, jpe, tif, tiff, webp, heic
        # > - Long text understanding: Supports doc/docx, xlsx, pdf, csv, txt
        self.file_url_object = file_url_object
        # - A unique knowledge base folder ID, used when you need to categorize documents and control the scope of documents for online Q&A queries.
        # - The folder ID needs to be obtained by logging into the intelligent document console.
        self.folder_id = folder_id
        # A unique extraction template ID used to specify the content to be extracted from the document. You need to log in to the template management page to configure the template and obtain the corresponding template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extract_type is not None:
            result['extractType'] = self.extract_type
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_url_object is not None:
            result['fileUrl'] = self.file_url_object
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extractType') is not None:
            self.extract_type = m.get('extractType')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileUrl') is not None:
            self.file_url_object = m.get('fileUrl')
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class SubmitDocExtractionTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # Task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class SubmitDocExtractionTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: SubmitDocExtractionTaskResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned data
        self.data = data
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = SubmitDocExtractionTaskResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class SubmitDocExtractionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitDocExtractionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitDocExtractionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDocParsingTaskRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_url: str = None,
        folder_id: str = None,
        need_analyze_img: bool = None,
    ):
        # The filename must include the file type extension.
        # 
        # This parameter is required.
        self.file_name = file_name
        # Choose one of fileUrl or fileUrlObject:
        # 
        # - fileUrl: Use by providing the document URL, for a single document (supports up to 1000 pages and 100MB in size)
        # 
        # - fileUrlObject: Use when calling the interface with local file upload, for a single document (supports up to 1000 pages and 100 MB in size)
        # 
        # > The relationship between file parsing methods and supported document types
        # > - Long Text RAG: Supports pdf, doc/docx, supports up to 1000 pages
        # > - Image Processing: Supports pdf, jpg, jpeg, png, bmp
        # > - Long Text Understanding: Supports pdf, doc/docx, xls/xlsx
        self.file_url = file_url
        # - Unique knowledge base folder ID, used when categorizing documents and controlling the scope of documents for online Q&A queries.
        # - The folder ID needs to be obtained from the Intelligent Document Console after logging in.
        self.folder_id = folder_id
        # Whether to parse image content within the document.
        self.need_analyze_img = need_analyze_img

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_url is not None:
            result['fileUrl'] = self.file_url
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        if self.need_analyze_img is not None:
            result['needAnalyzeImg'] = self.need_analyze_img
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        if m.get('needAnalyzeImg') is not None:
            self.need_analyze_img = m.get('needAnalyzeImg')
        return self


class SubmitDocParsingTaskAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        folder_id: str = None,
        need_analyze_img: bool = None,
    ):
        # The filename must include the file type extension.
        # 
        # This parameter is required.
        self.file_name = file_name
        # Choose one of fileUrl or fileUrlObject:
        # 
        # - fileUrl: Use by providing the document URL, for a single document (supports up to 1000 pages and 100MB in size)
        # 
        # - fileUrlObject: Use when calling the interface with local file upload, for a single document (supports up to 1000 pages and 100 MB in size)
        # 
        # > The relationship between file parsing methods and supported document types
        # > - Long Text RAG: Supports pdf, doc/docx, supports up to 1000 pages
        # > - Image Processing: Supports pdf, jpg, jpeg, png, bmp
        # > - Long Text Understanding: Supports pdf, doc/docx, xls/xlsx
        self.file_url_object = file_url_object
        # - Unique knowledge base folder ID, used when categorizing documents and controlling the scope of documents for online Q&A queries.
        # - The folder ID needs to be obtained from the Intelligent Document Console after logging in.
        self.folder_id = folder_id
        # Whether to parse image content within the document.
        self.need_analyze_img = need_analyze_img

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_url_object is not None:
            result['fileUrl'] = self.file_url_object
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        if self.need_analyze_img is not None:
            result['needAnalyzeImg'] = self.need_analyze_img
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileUrl') is not None:
            self.file_url_object = m.get('fileUrl')
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        if m.get('needAnalyzeImg') is not None:
            self.need_analyze_img = m.get('needAnalyzeImg')
        return self


class SubmitDocParsingTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # TaskID
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class SubmitDocParsingTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: SubmitDocParsingTaskResponseBodyData = None,
        request_id: str = None,
    ):
        # Return result.
        self.data = data
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = SubmitDocParsingTaskResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class SubmitDocParsingTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitDocParsingTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitDocParsingTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDocumentAnalyzeJobRequest(TeaModel):
    def __init__(
        self,
        analysis_type: str = None,
        file_name: str = None,
        file_url: str = None,
        folder_id: str = None,
        template_id: str = None,
    ):
        # The default extraction method is "doc", with the following optional values:
        # 
        # - vl: Image processing
        # - doc: Long text RAG (Retrieval-Augmented Generation)
        # - docUnderstanding: Long text comprehension
        # - recommender: Recommendation type
        self.analysis_type = analysis_type
        # The filename must include the file type extension.
        # 
        # This parameter is required.
        self.file_name = file_name
        # Choose one between fileUrl and fileUrlObject:
        # 
        # - fileUrl: Use the document URL method for a single document (supports documents with up to 1000 pages and within 100MB).
        # 
        # - fileUrlObject: Use when calling the API via local file upload, for a single document (supports documents with up to 1000 pages and 
        # within 100MB).
        # 
        # > Relationship between file parsing methods and supported document types. 
        # >- Long Text RAG: Supports pdf, doc/docx, and up to 1000 pages
        # >- Image Processing: Supports pdf, jpg, jpeg, png, bmp
        # >- Long Text Understanding: Supports pdf, doc/docx, xls/xlsx
        self.file_url = file_url
        # Unique knowledge base folder ID, used for categorizing documents and controlling the scope of online Q&A queries. If empty, the document will be uploaded to the tenant\\"s root directory.
        self.folder_id = folder_id
        # The unique extraction template ID is used to specify the key-value pairs to be extracted from the document. You need to log in to the template management page to configure the template and obtain the corresponding template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_type is not None:
            result['analysisType'] = self.analysis_type
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_url is not None:
            result['fileUrl'] = self.file_url
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisType') is not None:
            self.analysis_type = m.get('analysisType')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class SubmitDocumentAnalyzeJobAdvanceRequest(TeaModel):
    def __init__(
        self,
        analysis_type: str = None,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        folder_id: str = None,
        template_id: str = None,
    ):
        # The default extraction method is "doc", with the following optional values:
        # 
        # - vl: Image processing
        # - doc: Long text RAG (Retrieval-Augmented Generation)
        # - docUnderstanding: Long text comprehension
        # - recommender: Recommendation type
        self.analysis_type = analysis_type
        # The filename must include the file type extension.
        # 
        # This parameter is required.
        self.file_name = file_name
        # Choose one between fileUrl and fileUrlObject:
        # 
        # - fileUrl: Use the document URL method for a single document (supports documents with up to 1000 pages and within 100MB).
        # 
        # - fileUrlObject: Use when calling the API via local file upload, for a single document (supports documents with up to 1000 pages and 
        # within 100MB).
        # 
        # > Relationship between file parsing methods and supported document types. 
        # >- Long Text RAG: Supports pdf, doc/docx, and up to 1000 pages
        # >- Image Processing: Supports pdf, jpg, jpeg, png, bmp
        # >- Long Text Understanding: Supports pdf, doc/docx, xls/xlsx
        self.file_url_object = file_url_object
        # Unique knowledge base folder ID, used for categorizing documents and controlling the scope of online Q&A queries. If empty, the document will be uploaded to the tenant\\"s root directory.
        self.folder_id = folder_id
        # The unique extraction template ID is used to specify the key-value pairs to be extracted from the document. You need to log in to the template management page to configure the template and obtain the corresponding template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_type is not None:
            result['analysisType'] = self.analysis_type
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_url_object is not None:
            result['fileUrl'] = self.file_url_object
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisType') is not None:
            self.analysis_type = m.get('analysisType')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileUrl') is not None:
            self.file_url_object = m.get('fileUrl')
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class SubmitDocumentAnalyzeJobResponseBodyData(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # The job ID.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['jobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        return self


class SubmitDocumentAnalyzeJobResponseBody(TeaModel):
    def __init__(
        self,
        data: SubmitDocumentAnalyzeJobResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = SubmitDocumentAnalyzeJobResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class SubmitDocumentAnalyzeJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitDocumentAnalyzeJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitDocumentAnalyzeJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitVLExtractionTaskRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_url: str = None,
        folder_id: str = None,
        template_id: str = None,
    ):
        # The filename must include the file type suffix.
        # 
        # This parameter is required.
        self.file_name = file_name
        # Choose one of fileUrl or fileUrlObject:
        # 
        # - fileUrl: Use by providing the document URL, for a single document (supports up to 1000 pages and 100MB in size)
        # 
        # - fileUrlObject: Use when calling the interface with local file upload, for a single document (supports up to 1000 pages and 100 MB in size)
        # 
        # > The relationship between file parsing methods and supported document types
        # > - Long Text RAG: Supports pdf, doc/docx, up to 1000 pages
        # > - Image Processing: Supports pdf, jpg, jpeg, png, bmp
        # > - Long Text Understanding: Supports pdf, doc/docx, xls/xlsx
        self.file_url = file_url
        # - Unique knowledge base folder ID, used when you need to categorize documents and control the scope of online Q&A queries.
        # - The folder ID needs to be obtained from the intelligent document console after logging in.
        self.folder_id = folder_id
        # Unique parsing template ID, used to specify the key-value pairs to be extracted from the document. You need to configure the template on the template management page and then obtain the corresponding template ID.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_url is not None:
            result['fileUrl'] = self.file_url
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class SubmitVLExtractionTaskAdvanceRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        folder_id: str = None,
        template_id: str = None,
    ):
        # The filename must include the file type suffix.
        # 
        # This parameter is required.
        self.file_name = file_name
        # Choose one of fileUrl or fileUrlObject:
        # 
        # - fileUrl: Use by providing the document URL, for a single document (supports up to 1000 pages and 100MB in size)
        # 
        # - fileUrlObject: Use when calling the interface with local file upload, for a single document (supports up to 1000 pages and 100 MB in size)
        # 
        # > The relationship between file parsing methods and supported document types
        # > - Long Text RAG: Supports pdf, doc/docx, up to 1000 pages
        # > - Image Processing: Supports pdf, jpg, jpeg, png, bmp
        # > - Long Text Understanding: Supports pdf, doc/docx, xls/xlsx
        self.file_url_object = file_url_object
        # - Unique knowledge base folder ID, used when you need to categorize documents and control the scope of online Q&A queries.
        # - The folder ID needs to be obtained from the intelligent document console after logging in.
        self.folder_id = folder_id
        # Unique parsing template ID, used to specify the key-value pairs to be extracted from the document. You need to configure the template on the template management page and then obtain the corresponding template ID.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_url_object is not None:
            result['fileUrl'] = self.file_url_object
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileUrl') is not None:
            self.file_url_object = m.get('fileUrl')
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class SubmitVLExtractionTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # Task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class SubmitVLExtractionTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: SubmitVLExtractionTaskResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned data structure.
        self.data = data
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = SubmitVLExtractionTaskResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class SubmitVLExtractionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitVLExtractionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitVLExtractionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


