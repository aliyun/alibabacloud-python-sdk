# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class Address(TeaModel):
    def __init__(
        self,
        address_line: str = None,
        city: str = None,
        country: str = None,
        district: str = None,
        language: str = None,
        province: str = None,
        township: str = None,
    ):
        # AddressLine
        self.address_line = address_line
        # City
        self.city = city
        # Country
        self.country = country
        # District
        self.district = district
        # Language
        self.language = language
        # Province
        self.province = province
        # Township
        self.township = township

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_line is not None:
            result['AddressLine'] = self.address_line
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.district is not None:
            result['District'] = self.district
        if self.language is not None:
            result['Language'] = self.language
        if self.province is not None:
            result['Province'] = self.province
        if self.township is not None:
            result['Township'] = self.township
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressLine') is not None:
            self.address_line = m.get('AddressLine')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Township') is not None:
            self.township = m.get('Township')
        return self


class AssumeRoleChainNode(TeaModel):
    def __init__(
        self,
        owner_id: str = None,
        role: str = None,
        type: str = None,
    ):
        # 账号id
        self.owner_id = owner_id
        # 授权角色名
        self.role = role
        # 账号类型，普通账号填 user，服务账号填 service
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.role is not None:
            result['Role'] = self.role
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AssumeRoleChain(TeaModel):
    def __init__(
        self,
        chain: List[AssumeRoleChainNode] = None,
        policy: str = None,
    ):
        # 链式授权节点
        self.chain = chain
        # 当前用户 policy
        self.policy = policy

    def validate(self):
        if self.chain:
            for k in self.chain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Chain'] = []
        if self.chain is not None:
            for k in self.chain:
                result['Chain'].append(k.to_map() if k else None)
        if self.policy is not None:
            result['Policy'] = self.policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chain = []
        if m.get('Chain') is not None:
            for k in m.get('Chain'):
                temp_model = AssumeRoleChainNode()
                self.chain.append(temp_model.from_map(k))
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        return self


class AudioStream(TeaModel):
    def __init__(
        self,
        bitrate: int = None,
        channel_layout: str = None,
        channels: int = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        duration: float = None,
        frame_count: int = None,
        index: int = None,
        language: str = None,
        lyric: str = None,
        sample_format: str = None,
        sample_rate: int = None,
        start_time: float = None,
        time_base: str = None,
    ):
        # Bitrate
        self.bitrate = bitrate
        # ChannelLayout
        self.channel_layout = channel_layout
        # Channels
        self.channels = channels
        # CodecLongName
        self.codec_long_name = codec_long_name
        # CodecName
        self.codec_name = codec_name
        # CodecTag
        self.codec_tag = codec_tag
        # CodecTagString
        self.codec_tag_string = codec_tag_string
        # CodecTimeBase
        self.codec_time_base = codec_time_base
        # Duration
        self.duration = duration
        # FrameCount
        self.frame_count = frame_count
        # Index
        self.index = index
        # Language
        self.language = language
        # Lyric
        self.lyric = lyric
        # SampleFormat
        self.sample_format = sample_format
        # SampleRate
        self.sample_rate = sample_rate
        # StartTime
        self.start_time = start_time
        # TimeBase
        self.time_base = time_base

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.channel_layout is not None:
            result['ChannelLayout'] = self.channel_layout
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.frame_count is not None:
            result['FrameCount'] = self.frame_count
        if self.index is not None:
            result['Index'] = self.index
        if self.language is not None:
            result['Language'] = self.language
        if self.lyric is not None:
            result['Lyric'] = self.lyric
        if self.sample_format is not None:
            result['SampleFormat'] = self.sample_format
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_base is not None:
            result['TimeBase'] = self.time_base
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('ChannelLayout') is not None:
            self.channel_layout = m.get('ChannelLayout')
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FrameCount') is not None:
            self.frame_count = m.get('FrameCount')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Lyric') is not None:
            self.lyric = m.get('Lyric')
        if m.get('SampleFormat') is not None:
            self.sample_format = m.get('SampleFormat')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeBase') is not None:
            self.time_base = m.get('TimeBase')
        return self


class Binding(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        dataset_name: str = None,
        detail: str = None,
        phase: str = None,
        project_name: str = None,
        state: str = None,
        uri: str = None,
        update_time: str = None,
    ):
        # CreateTime
        self.create_time = create_time
        # DatasetName
        self.dataset_name = dataset_name
        # Detail
        self.detail = detail
        # Phase
        self.phase = phase
        # ProjectName
        self.project_name = project_name
        # State
        self.state = state
        # URI
        self.uri = uri
        # UpdateTime
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.state is not None:
            result['State'] = self.state
        if self.uri is not None:
            result['URI'] = self.uri
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class Boundary(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        # Height
        self.height = height
        # Left
        self.left = left
        # Top
        self.top = top
        # Width
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class Body(TeaModel):
    def __init__(
        self,
        boundary: Boundary = None,
        confidence: float = None,
    ):
        # Boundary
        self.boundary = boundary
        # Confidence
        self.confidence = confidence

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class ClusterForReqCoverFigures(TeaModel):
    def __init__(
        self,
        figure_id: str = None,
    ):
        # FigureId
        self.figure_id = figure_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        return self


class ClusterForReqCover(TeaModel):
    def __init__(
        self,
        figures: List[ClusterForReqCoverFigures] = None,
    ):
        # Figures
        self.figures = figures

    def validate(self):
        if self.figures:
            for k in self.figures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Figures'] = []
        if self.figures is not None:
            for k in self.figures:
                result['Figures'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.figures = []
        if m.get('Figures') is not None:
            for k in m.get('Figures'):
                temp_model = ClusterForReqCoverFigures()
                self.figures.append(temp_model.from_map(k))
        return self


class ClusterForReq(TeaModel):
    def __init__(
        self,
        cover: ClusterForReqCover = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        name: str = None,
        object_id: str = None,
    ):
        # Cover
        self.cover = cover
        # CustomId
        self.custom_id = custom_id
        # CustomLabels
        self.custom_labels = custom_labels
        # Name
        self.name = name
        # ObjectId
        self.object_id = object_id

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.name is not None:
            result['Name'] = self.name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cover') is not None:
            temp_model = ClusterForReqCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        return self


class Codes(TeaModel):
    def __init__(
        self,
        boundary: Boundary = None,
        confidence: float = None,
        content: str = None,
        type: str = None,
    ):
        # Boundary
        self.boundary = boundary
        # Confidence
        self.confidence = confidence
        # Content
        self.content = content
        # Type
        self.type = type

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.content is not None:
            result['Content'] = self.content
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CredentialConfigChain(TeaModel):
    def __init__(
        self,
        assume_role_for: str = None,
        role: str = None,
        role_type: str = None,
    ):
        # 授权对象
        self.assume_role_for = assume_role_for
        # 授权角色
        self.role = role
        # 授权方类型
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for
        if self.role is not None:
            result['Role'] = self.role
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class CredentialConfig(TeaModel):
    def __init__(
        self,
        chain: List[CredentialConfigChain] = None,
        policy: str = None,
        service_role: str = None,
    ):
        # 授权链
        self.chain = chain
        # 权限策略
        self.policy = policy
        # 服务角色
        self.service_role = service_role

    def validate(self):
        if self.chain:
            for k in self.chain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Chain'] = []
        if self.chain is not None:
            for k in self.chain:
                result['Chain'].append(k.to_map() if k else None)
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chain = []
        if m.get('Chain') is not None:
            for k in m.get('Chain'):
                temp_model = CredentialConfigChain()
                self.chain.append(temp_model.from_map(k))
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        return self


class CroppingSuggestion(TeaModel):
    def __init__(
        self,
        aspect_ratio: str = None,
        boundary: Boundary = None,
        confidence: float = None,
    ):
        # AspectRatio
        self.aspect_ratio = aspect_ratio
        # Boundary
        self.boundary = boundary
        # Confidence
        self.confidence = confidence

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class Dataset(TeaModel):
    def __init__(
        self,
        bind_count: int = None,
        create_time: str = None,
        dataset_max_bind_count: int = None,
        dataset_max_entity_count: int = None,
        dataset_max_file_count: int = None,
        dataset_max_relation_count: int = None,
        dataset_max_total_file_size: int = None,
        dataset_name: str = None,
        description: str = None,
        file_count: int = None,
        project_name: str = None,
        total_file_size: int = None,
        update_time: str = None,
    ):
        # 媒体集当前绑定数
        self.bind_count = bind_count
        # 创建时间
        self.create_time = create_time
        # 媒体集最大绑定数
        self.dataset_max_bind_count = dataset_max_bind_count
        # 媒体集最多实体数量
        self.dataset_max_entity_count = dataset_max_entity_count
        # 媒体集最多文件数量
        self.dataset_max_file_count = dataset_max_file_count
        # 媒体集最多关系数量
        self.dataset_max_relation_count = dataset_max_relation_count
        # 媒体集最大文件总大小
        self.dataset_max_total_file_size = dataset_max_total_file_size
        # 媒体集名称
        self.dataset_name = dataset_name
        # 描述
        self.description = description
        # 媒体集当前文件数
        self.file_count = file_count
        # 项目名称
        self.project_name = project_name
        # 媒体集当前文件总大小
        self.total_file_size = total_file_size
        # 更新时间
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_count is not None:
            result['BindCount'] = self.bind_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.file_count is not None:
            result['FileCount'] = self.file_count
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.total_file_size is not None:
            result['TotalFileSize'] = self.total_file_size
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindCount') is not None:
            self.bind_count = m.get('BindCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TotalFileSize') is not None:
            self.total_file_size = m.get('TotalFileSize')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class HeadPose(TeaModel):
    def __init__(
        self,
        pitch: float = None,
        roll: float = None,
        yaw: float = None,
    ):
        # Pitch
        self.pitch = pitch
        # Roll
        self.roll = roll
        # Yaw
        self.yaw = yaw

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch is not None:
            result['Pitch'] = self.pitch
        if self.roll is not None:
            result['Roll'] = self.roll
        if self.yaw is not None:
            result['Yaw'] = self.yaw
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')
        if m.get('Roll') is not None:
            self.roll = m.get('Roll')
        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')
        return self


class Figure(TeaModel):
    def __init__(
        self,
        age: int = None,
        age_sd: float = None,
        attractive: float = None,
        beard: str = None,
        beard_confidence: float = None,
        boundary: Boundary = None,
        emotion: str = None,
        emotion_confidence: float = None,
        face_quality: float = None,
        figure_cluster_confidence: float = None,
        figure_cluster_id: str = None,
        figure_confidence: float = None,
        figure_id: str = None,
        figure_type: str = None,
        gender: str = None,
        gender_confidence: float = None,
        glasses: str = None,
        glasses_confidence: float = None,
        hat: str = None,
        hat_confidence: float = None,
        head_pose: HeadPose = None,
        mask: str = None,
        mask_confidence: float = None,
        mouth: str = None,
        mouth_confidence: float = None,
        sharpness: float = None,
    ):
        # Age
        self.age = age
        # AgeSD
        self.age_sd = age_sd
        # Attractive
        self.attractive = attractive
        # Beard
        self.beard = beard
        # BeardConfidence
        self.beard_confidence = beard_confidence
        # Boundary
        self.boundary = boundary
        # Emotion
        self.emotion = emotion
        # EmotionConfidence
        self.emotion_confidence = emotion_confidence
        # FaceQuality
        self.face_quality = face_quality
        # FigureClusterConfidence
        self.figure_cluster_confidence = figure_cluster_confidence
        # FigureClusterId
        self.figure_cluster_id = figure_cluster_id
        # FigureConfidence
        self.figure_confidence = figure_confidence
        # FigureId
        self.figure_id = figure_id
        # FigureType
        self.figure_type = figure_type
        # Gender
        self.gender = gender
        # GenderConfidence
        self.gender_confidence = gender_confidence
        # Glasses
        self.glasses = glasses
        # GlassesConfidence
        self.glasses_confidence = glasses_confidence
        # Hat
        self.hat = hat
        # HatConfidence
        self.hat_confidence = hat_confidence
        self.head_pose = head_pose
        # Mask
        self.mask = mask
        # MaskConfidence
        self.mask_confidence = mask_confidence
        # Mouth
        self.mouth = mouth
        # MouthConfidence
        self.mouth_confidence = mouth_confidence
        # Sharpness
        self.sharpness = sharpness

    def validate(self):
        if self.boundary:
            self.boundary.validate()
        if self.head_pose:
            self.head_pose.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.age is not None:
            result['Age'] = self.age
        if self.age_sd is not None:
            result['AgeSD'] = self.age_sd
        if self.attractive is not None:
            result['Attractive'] = self.attractive
        if self.beard is not None:
            result['Beard'] = self.beard
        if self.beard_confidence is not None:
            result['BeardConfidence'] = self.beard_confidence
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.emotion_confidence is not None:
            result['EmotionConfidence'] = self.emotion_confidence
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.figure_cluster_confidence is not None:
            result['FigureClusterConfidence'] = self.figure_cluster_confidence
        if self.figure_cluster_id is not None:
            result['FigureClusterId'] = self.figure_cluster_id
        if self.figure_confidence is not None:
            result['FigureConfidence'] = self.figure_confidence
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        if self.figure_type is not None:
            result['FigureType'] = self.figure_type
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.gender_confidence is not None:
            result['GenderConfidence'] = self.gender_confidence
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.glasses_confidence is not None:
            result['GlassesConfidence'] = self.glasses_confidence
        if self.hat is not None:
            result['Hat'] = self.hat
        if self.hat_confidence is not None:
            result['HatConfidence'] = self.hat_confidence
        if self.head_pose is not None:
            result['HeadPose'] = self.head_pose.to_map()
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.mask_confidence is not None:
            result['MaskConfidence'] = self.mask_confidence
        if self.mouth is not None:
            result['Mouth'] = self.mouth
        if self.mouth_confidence is not None:
            result['MouthConfidence'] = self.mouth_confidence
        if self.sharpness is not None:
            result['Sharpness'] = self.sharpness
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('AgeSD') is not None:
            self.age_sd = m.get('AgeSD')
        if m.get('Attractive') is not None:
            self.attractive = m.get('Attractive')
        if m.get('Beard') is not None:
            self.beard = m.get('Beard')
        if m.get('BeardConfidence') is not None:
            self.beard_confidence = m.get('BeardConfidence')
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('EmotionConfidence') is not None:
            self.emotion_confidence = m.get('EmotionConfidence')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('FigureClusterConfidence') is not None:
            self.figure_cluster_confidence = m.get('FigureClusterConfidence')
        if m.get('FigureClusterId') is not None:
            self.figure_cluster_id = m.get('FigureClusterId')
        if m.get('FigureConfidence') is not None:
            self.figure_confidence = m.get('FigureConfidence')
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        if m.get('FigureType') is not None:
            self.figure_type = m.get('FigureType')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('GenderConfidence') is not None:
            self.gender_confidence = m.get('GenderConfidence')
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('GlassesConfidence') is not None:
            self.glasses_confidence = m.get('GlassesConfidence')
        if m.get('Hat') is not None:
            self.hat = m.get('Hat')
        if m.get('HatConfidence') is not None:
            self.hat_confidence = m.get('HatConfidence')
        if m.get('HeadPose') is not None:
            temp_model = HeadPose()
            self.head_pose = temp_model.from_map(m['HeadPose'])
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('MaskConfidence') is not None:
            self.mask_confidence = m.get('MaskConfidence')
        if m.get('Mouth') is not None:
            self.mouth = m.get('Mouth')
        if m.get('MouthConfidence') is not None:
            self.mouth_confidence = m.get('MouthConfidence')
        if m.get('Sharpness') is not None:
            self.sharpness = m.get('Sharpness')
        return self


class ImageScore(TeaModel):
    def __init__(
        self,
        overall_quality_score: float = None,
    ):
        # OverallQualityScore
        self.overall_quality_score = overall_quality_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overall_quality_score is not None:
            result['OverallQualityScore'] = self.overall_quality_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverallQualityScore') is not None:
            self.overall_quality_score = m.get('OverallQualityScore')
        return self


class OCRContents(TeaModel):
    def __init__(
        self,
        boundary: Boundary = None,
        confidence: float = None,
        contents: str = None,
        language: str = None,
    ):
        # Boundary
        self.boundary = boundary
        # Confidence
        self.confidence = confidence
        # Contents
        self.contents = contents
        # Language
        self.language = language

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.contents is not None:
            result['Contents'] = self.contents
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class Image(TeaModel):
    def __init__(
        self,
        cropping_suggestions: List[CroppingSuggestion] = None,
        exif: str = None,
        image_height: int = None,
        image_score: ImageScore = None,
        image_width: int = None,
        ocrcontents: List[OCRContents] = None,
    ):
        # CroppingSuggestions
        self.cropping_suggestions = cropping_suggestions
        # EXIF
        self.exif = exif
        # ImageHeight
        self.image_height = image_height
        self.image_score = image_score
        # ImageWidth
        self.image_width = image_width
        # OCRContents
        self.ocrcontents = ocrcontents

    def validate(self):
        if self.cropping_suggestions:
            for k in self.cropping_suggestions:
                if k:
                    k.validate()
        if self.image_score:
            self.image_score.validate()
        if self.ocrcontents:
            for k in self.ocrcontents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CroppingSuggestions'] = []
        if self.cropping_suggestions is not None:
            for k in self.cropping_suggestions:
                result['CroppingSuggestions'].append(k.to_map() if k else None)
        if self.exif is not None:
            result['EXIF'] = self.exif
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.image_score is not None:
            result['ImageScore'] = self.image_score.to_map()
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        result['OCRContents'] = []
        if self.ocrcontents is not None:
            for k in self.ocrcontents:
                result['OCRContents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cropping_suggestions = []
        if m.get('CroppingSuggestions') is not None:
            for k in m.get('CroppingSuggestions'):
                temp_model = CroppingSuggestion()
                self.cropping_suggestions.append(temp_model.from_map(k))
        if m.get('EXIF') is not None:
            self.exif = m.get('EXIF')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ImageScore') is not None:
            temp_model = ImageScore()
            self.image_score = temp_model.from_map(m['ImageScore'])
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        self.ocrcontents = []
        if m.get('OCRContents') is not None:
            for k in m.get('OCRContents'):
                temp_model = OCRContents()
                self.ocrcontents.append(temp_model.from_map(k))
        return self


class Label(TeaModel):
    def __init__(
        self,
        centric_score: float = None,
        label_confidence: float = None,
        label_level: int = None,
        label_name: str = None,
        language: str = None,
        parent_label_name: str = None,
    ):
        # CentricScore
        self.centric_score = centric_score
        # LabelConfidence
        self.label_confidence = label_confidence
        # LabelLevel
        self.label_level = label_level
        # LabelName
        self.label_name = label_name
        # Language
        self.language = language
        # ParentLabelName
        self.parent_label_name = parent_label_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.centric_score is not None:
            result['CentricScore'] = self.centric_score
        if self.label_confidence is not None:
            result['LabelConfidence'] = self.label_confidence
        if self.label_level is not None:
            result['LabelLevel'] = self.label_level
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        if self.language is not None:
            result['Language'] = self.language
        if self.parent_label_name is not None:
            result['ParentLabelName'] = self.parent_label_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CentricScore') is not None:
            self.centric_score = m.get('CentricScore')
        if m.get('LabelConfidence') is not None:
            self.label_confidence = m.get('LabelConfidence')
        if m.get('LabelLevel') is not None:
            self.label_level = m.get('LabelLevel')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ParentLabelName') is not None:
            self.parent_label_name = m.get('ParentLabelName')
        return self


class SubtitleStream(TeaModel):
    def __init__(
        self,
        bitrate: int = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        content: str = None,
        duration: float = None,
        height: int = None,
        index: int = None,
        language: str = None,
        start_time: float = None,
        width: int = None,
    ):
        # Bitrate
        self.bitrate = bitrate
        # CodecLongName
        self.codec_long_name = codec_long_name
        # CodecName
        self.codec_name = codec_name
        # CodecTag
        self.codec_tag = codec_tag
        # CodecTagString
        self.codec_tag_string = codec_tag_string
        # Content
        self.content = content
        # Duration
        self.duration = duration
        # Height
        self.height = height
        # Index
        self.index = index
        # Language
        self.language = language
        # StartTime
        self.start_time = start_time
        # Width
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.content is not None:
            result['Content'] = self.content
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.height is not None:
            result['Height'] = self.height
        if self.index is not None:
            result['Index'] = self.index
        if self.language is not None:
            result['Language'] = self.language
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class VideoStream(TeaModel):
    def __init__(
        self,
        average_frame_rate: str = None,
        bit_depth: int = None,
        bitrate: int = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        color_primaries: str = None,
        color_range: str = None,
        color_space: str = None,
        color_transfer: str = None,
        display_aspect_ratio: str = None,
        duration: float = None,
        frame_count: int = None,
        frame_rate: str = None,
        has_bframes: int = None,
        height: int = None,
        index: int = None,
        language: str = None,
        level: int = None,
        pixel_format: str = None,
        profile: str = None,
        rotate: str = None,
        sample_aspect_ratio: str = None,
        start_time: float = None,
        time_base: str = None,
        width: int = None,
    ):
        # AverageFrameRate
        self.average_frame_rate = average_frame_rate
        # BitDepth
        self.bit_depth = bit_depth
        # Bitrate
        self.bitrate = bitrate
        # CodecLongName
        self.codec_long_name = codec_long_name
        # CodecName
        self.codec_name = codec_name
        # CodecTag
        self.codec_tag = codec_tag
        # CodecTagString
        self.codec_tag_string = codec_tag_string
        # CodecTimeBase
        self.codec_time_base = codec_time_base
        # ColorPrimaries
        self.color_primaries = color_primaries
        # ColorRange
        self.color_range = color_range
        # ColorSpace
        self.color_space = color_space
        # ColorTransfer
        self.color_transfer = color_transfer
        # DisplayAspectRatio
        self.display_aspect_ratio = display_aspect_ratio
        # Duration
        self.duration = duration
        # FrameCount
        self.frame_count = frame_count
        # FrameRate
        self.frame_rate = frame_rate
        # HasBFrames
        self.has_bframes = has_bframes
        # Height
        self.height = height
        # Index
        self.index = index
        # Language
        self.language = language
        # Level
        self.level = level
        # PixelFormat
        self.pixel_format = pixel_format
        # Profile
        self.profile = profile
        # Rotate
        self.rotate = rotate
        # SampleAspectRatio
        self.sample_aspect_ratio = sample_aspect_ratio
        # StartTime
        self.start_time = start_time
        # TimeBase
        self.time_base = time_base
        # Width
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average_frame_rate is not None:
            result['AverageFrameRate'] = self.average_frame_rate
        if self.bit_depth is not None:
            result['BitDepth'] = self.bit_depth
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.color_primaries is not None:
            result['ColorPrimaries'] = self.color_primaries
        if self.color_range is not None:
            result['ColorRange'] = self.color_range
        if self.color_space is not None:
            result['ColorSpace'] = self.color_space
        if self.color_transfer is not None:
            result['ColorTransfer'] = self.color_transfer
        if self.display_aspect_ratio is not None:
            result['DisplayAspectRatio'] = self.display_aspect_ratio
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.frame_count is not None:
            result['FrameCount'] = self.frame_count
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.has_bframes is not None:
            result['HasBFrames'] = self.has_bframes
        if self.height is not None:
            result['Height'] = self.height
        if self.index is not None:
            result['Index'] = self.index
        if self.language is not None:
            result['Language'] = self.language
        if self.level is not None:
            result['Level'] = self.level
        if self.pixel_format is not None:
            result['PixelFormat'] = self.pixel_format
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.sample_aspect_ratio is not None:
            result['SampleAspectRatio'] = self.sample_aspect_ratio
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_base is not None:
            result['TimeBase'] = self.time_base
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageFrameRate') is not None:
            self.average_frame_rate = m.get('AverageFrameRate')
        if m.get('BitDepth') is not None:
            self.bit_depth = m.get('BitDepth')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('ColorPrimaries') is not None:
            self.color_primaries = m.get('ColorPrimaries')
        if m.get('ColorRange') is not None:
            self.color_range = m.get('ColorRange')
        if m.get('ColorSpace') is not None:
            self.color_space = m.get('ColorSpace')
        if m.get('ColorTransfer') is not None:
            self.color_transfer = m.get('ColorTransfer')
        if m.get('DisplayAspectRatio') is not None:
            self.display_aspect_ratio = m.get('DisplayAspectRatio')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FrameCount') is not None:
            self.frame_count = m.get('FrameCount')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('HasBFrames') is not None:
            self.has_bframes = m.get('HasBFrames')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PixelFormat') is not None:
            self.pixel_format = m.get('PixelFormat')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('SampleAspectRatio') is not None:
            self.sample_aspect_ratio = m.get('SampleAspectRatio')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeBase') is not None:
            self.time_base = m.get('TimeBase')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class File(TeaModel):
    def __init__(
        self,
        access_control_allow_origin: str = None,
        access_control_request_method: str = None,
        addresses: List[Address] = None,
        album: str = None,
        album_artist: str = None,
        artist: str = None,
        audio_covers: List[Image] = None,
        audio_streams: List[AudioStream] = None,
        bitrate: int = None,
        cache_control: str = None,
        composer: str = None,
        content_disposition: str = None,
        content_encoding: str = None,
        content_language: str = None,
        content_md_5: str = None,
        content_type: str = None,
        create_time: str = None,
        cropping_suggestions: List[CroppingSuggestion] = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        dataset_name: str = None,
        document_content: str = None,
        document_language: str = None,
        duration: float = None,
        etag: str = None,
        exif: str = None,
        figure_count: int = None,
        figures: List[Figure] = None,
        file_access_time: str = None,
        file_create_time: str = None,
        file_hash: str = None,
        file_modified_time: str = None,
        filename: str = None,
        format_long_name: str = None,
        format_name: str = None,
        image_height: int = None,
        image_score: ImageScore = None,
        image_width: int = None,
        labels: List[Label] = None,
        language: str = None,
        lat_long: str = None,
        media_type: str = None,
        ocrcontents: List[OCRContents] = None,
        osscrc64: str = None,
        ossdelete_marker: str = None,
        ossexpiration: str = None,
        ossobject_type: str = None,
        ossstorage_class: str = None,
        osstagging: Dict[str, Any] = None,
        osstagging_count: int = None,
        ossuri: str = None,
        ossuser_meta: Dict[str, Any] = None,
        ossversion_id: str = None,
        object_acl: str = None,
        object_id: str = None,
        object_type: str = None,
        orientation: int = None,
        owner_id: str = None,
        page_count: int = None,
        performer: str = None,
        produce_time: str = None,
        program_count: int = None,
        project_name: str = None,
        server_side_data_encryption: str = None,
        server_side_encryption: str = None,
        server_side_encryption_customer_algorithm: str = None,
        server_side_encryption_key_id: str = None,
        size: int = None,
        start_time: float = None,
        stream_count: int = None,
        subtitles: List[SubtitleStream] = None,
        timezone: str = None,
        title: str = None,
        travel_cluster_id: str = None,
        uri: str = None,
        update_time: str = None,
        video_height: int = None,
        video_streams: List[VideoStream] = None,
        video_width: int = None,
    ):
        # AccessControlAllowOrigin
        self.access_control_allow_origin = access_control_allow_origin
        # AccessControlRequestMethod
        self.access_control_request_method = access_control_request_method
        # Addresses
        self.addresses = addresses
        # Album
        self.album = album
        # AlbumArtist
        self.album_artist = album_artist
        # Artist
        self.artist = artist
        # AudioCovers
        self.audio_covers = audio_covers
        # AudioStreams
        self.audio_streams = audio_streams
        # Bitrate
        self.bitrate = bitrate
        # CacheControl
        self.cache_control = cache_control
        # Composer
        self.composer = composer
        # ContentDisposition
        self.content_disposition = content_disposition
        # ContentEncoding
        self.content_encoding = content_encoding
        # ContentLanguage
        self.content_language = content_language
        # ContentMd5
        self.content_md_5 = content_md_5
        # ContentType
        self.content_type = content_type
        # CreateTime
        self.create_time = create_time
        # CroppingSuggestions
        self.cropping_suggestions = cropping_suggestions
        # CustomId
        self.custom_id = custom_id
        # CustomLabels
        self.custom_labels = custom_labels
        # DatasetName
        self.dataset_name = dataset_name
        # DocumentContent
        self.document_content = document_content
        # DocumentLanguage
        self.document_language = document_language
        # Duration
        self.duration = duration
        # ETag
        self.etag = etag
        # EXIF
        self.exif = exif
        # FigureCount
        self.figure_count = figure_count
        # Figures
        self.figures = figures
        # FileAccessTime
        self.file_access_time = file_access_time
        # FileCreateTime
        self.file_create_time = file_create_time
        # FileHash
        self.file_hash = file_hash
        # FileModifiedTime
        self.file_modified_time = file_modified_time
        # Filename
        self.filename = filename
        # FormatLongName
        self.format_long_name = format_long_name
        # FormatName
        self.format_name = format_name
        # ImageHeight
        self.image_height = image_height
        self.image_score = image_score
        # ImageWidth
        self.image_width = image_width
        # Labels
        self.labels = labels
        # Language
        self.language = language
        # LatLong
        self.lat_long = lat_long
        # MediaType
        self.media_type = media_type
        # OCRContents
        self.ocrcontents = ocrcontents
        # OSSCRC64
        self.osscrc64 = osscrc64
        # OSSDeleteMarker
        self.ossdelete_marker = ossdelete_marker
        # OSSExpiration
        self.ossexpiration = ossexpiration
        # OSSObjectType
        self.ossobject_type = ossobject_type
        # OSSStorageClass
        self.ossstorage_class = ossstorage_class
        # OSSTagging
        self.osstagging = osstagging
        # OSSTaggingCount
        self.osstagging_count = osstagging_count
        # OSSURI
        self.ossuri = ossuri
        # OSSUserMeta
        self.ossuser_meta = ossuser_meta
        # OSSVersionId
        self.ossversion_id = ossversion_id
        # ObjectACL
        self.object_acl = object_acl
        # ObjectId
        self.object_id = object_id
        # ObjectType
        self.object_type = object_type
        # Orientation
        self.orientation = orientation
        # OwnerId
        self.owner_id = owner_id
        # PageCount
        self.page_count = page_count
        # Performer
        self.performer = performer
        # ProduceTime
        self.produce_time = produce_time
        # ProgramCount
        self.program_count = program_count
        # ProjectName
        self.project_name = project_name
        # ServerSideDataEncryption
        self.server_side_data_encryption = server_side_data_encryption
        # ServerSideEncryption
        self.server_side_encryption = server_side_encryption
        # ServerSideEncryptionCustomerAlgorithm
        self.server_side_encryption_customer_algorithm = server_side_encryption_customer_algorithm
        # ServerSideEncryptionKeyId
        self.server_side_encryption_key_id = server_side_encryption_key_id
        # Size
        self.size = size
        # StartTime
        self.start_time = start_time
        # StreamCount
        self.stream_count = stream_count
        # Subtitles
        self.subtitles = subtitles
        # Timezone
        self.timezone = timezone
        # Title
        self.title = title
        # TravelClusterId
        self.travel_cluster_id = travel_cluster_id
        # URI
        self.uri = uri
        # UpdateTime
        self.update_time = update_time
        # VideoHeight
        self.video_height = video_height
        # VideoStreams
        self.video_streams = video_streams
        # VideoWidth
        self.video_width = video_width

    def validate(self):
        if self.addresses:
            for k in self.addresses:
                if k:
                    k.validate()
        if self.audio_covers:
            for k in self.audio_covers:
                if k:
                    k.validate()
        if self.audio_streams:
            for k in self.audio_streams:
                if k:
                    k.validate()
        if self.cropping_suggestions:
            for k in self.cropping_suggestions:
                if k:
                    k.validate()
        if self.figures:
            for k in self.figures:
                if k:
                    k.validate()
        if self.image_score:
            self.image_score.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.ocrcontents:
            for k in self.ocrcontents:
                if k:
                    k.validate()
        if self.subtitles:
            for k in self.subtitles:
                if k:
                    k.validate()
        if self.video_streams:
            for k in self.video_streams:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_allow_origin is not None:
            result['AccessControlAllowOrigin'] = self.access_control_allow_origin
        if self.access_control_request_method is not None:
            result['AccessControlRequestMethod'] = self.access_control_request_method
        result['Addresses'] = []
        if self.addresses is not None:
            for k in self.addresses:
                result['Addresses'].append(k.to_map() if k else None)
        if self.album is not None:
            result['Album'] = self.album
        if self.album_artist is not None:
            result['AlbumArtist'] = self.album_artist
        if self.artist is not None:
            result['Artist'] = self.artist
        result['AudioCovers'] = []
        if self.audio_covers is not None:
            for k in self.audio_covers:
                result['AudioCovers'].append(k.to_map() if k else None)
        result['AudioStreams'] = []
        if self.audio_streams is not None:
            for k in self.audio_streams:
                result['AudioStreams'].append(k.to_map() if k else None)
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.cache_control is not None:
            result['CacheControl'] = self.cache_control
        if self.composer is not None:
            result['Composer'] = self.composer
        if self.content_disposition is not None:
            result['ContentDisposition'] = self.content_disposition
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.content_language is not None:
            result['ContentLanguage'] = self.content_language
        if self.content_md_5 is not None:
            result['ContentMd5'] = self.content_md_5
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['CroppingSuggestions'] = []
        if self.cropping_suggestions is not None:
            for k in self.cropping_suggestions:
                result['CroppingSuggestions'].append(k.to_map() if k else None)
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.document_content is not None:
            result['DocumentContent'] = self.document_content
        if self.document_language is not None:
            result['DocumentLanguage'] = self.document_language
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.exif is not None:
            result['EXIF'] = self.exif
        if self.figure_count is not None:
            result['FigureCount'] = self.figure_count
        result['Figures'] = []
        if self.figures is not None:
            for k in self.figures:
                result['Figures'].append(k.to_map() if k else None)
        if self.file_access_time is not None:
            result['FileAccessTime'] = self.file_access_time
        if self.file_create_time is not None:
            result['FileCreateTime'] = self.file_create_time
        if self.file_hash is not None:
            result['FileHash'] = self.file_hash
        if self.file_modified_time is not None:
            result['FileModifiedTime'] = self.file_modified_time
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.format_long_name is not None:
            result['FormatLongName'] = self.format_long_name
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.image_score is not None:
            result['ImageScore'] = self.image_score.to_map()
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.language is not None:
            result['Language'] = self.language
        if self.lat_long is not None:
            result['LatLong'] = self.lat_long
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        result['OCRContents'] = []
        if self.ocrcontents is not None:
            for k in self.ocrcontents:
                result['OCRContents'].append(k.to_map() if k else None)
        if self.osscrc64 is not None:
            result['OSSCRC64'] = self.osscrc64
        if self.ossdelete_marker is not None:
            result['OSSDeleteMarker'] = self.ossdelete_marker
        if self.ossexpiration is not None:
            result['OSSExpiration'] = self.ossexpiration
        if self.ossobject_type is not None:
            result['OSSObjectType'] = self.ossobject_type
        if self.ossstorage_class is not None:
            result['OSSStorageClass'] = self.ossstorage_class
        if self.osstagging is not None:
            result['OSSTagging'] = self.osstagging
        if self.osstagging_count is not None:
            result['OSSTaggingCount'] = self.osstagging_count
        if self.ossuri is not None:
            result['OSSURI'] = self.ossuri
        if self.ossuser_meta is not None:
            result['OSSUserMeta'] = self.ossuser_meta
        if self.ossversion_id is not None:
            result['OSSVersionId'] = self.ossversion_id
        if self.object_acl is not None:
            result['ObjectACL'] = self.object_acl
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.orientation is not None:
            result['Orientation'] = self.orientation
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.performer is not None:
            result['Performer'] = self.performer
        if self.produce_time is not None:
            result['ProduceTime'] = self.produce_time
        if self.program_count is not None:
            result['ProgramCount'] = self.program_count
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.server_side_data_encryption is not None:
            result['ServerSideDataEncryption'] = self.server_side_data_encryption
        if self.server_side_encryption is not None:
            result['ServerSideEncryption'] = self.server_side_encryption
        if self.server_side_encryption_customer_algorithm is not None:
            result['ServerSideEncryptionCustomerAlgorithm'] = self.server_side_encryption_customer_algorithm
        if self.server_side_encryption_key_id is not None:
            result['ServerSideEncryptionKeyId'] = self.server_side_encryption_key_id
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_count is not None:
            result['StreamCount'] = self.stream_count
        result['Subtitles'] = []
        if self.subtitles is not None:
            for k in self.subtitles:
                result['Subtitles'].append(k.to_map() if k else None)
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.title is not None:
            result['Title'] = self.title
        if self.travel_cluster_id is not None:
            result['TravelClusterId'] = self.travel_cluster_id
        if self.uri is not None:
            result['URI'] = self.uri
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.video_height is not None:
            result['VideoHeight'] = self.video_height
        result['VideoStreams'] = []
        if self.video_streams is not None:
            for k in self.video_streams:
                result['VideoStreams'].append(k.to_map() if k else None)
        if self.video_width is not None:
            result['VideoWidth'] = self.video_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessControlAllowOrigin') is not None:
            self.access_control_allow_origin = m.get('AccessControlAllowOrigin')
        if m.get('AccessControlRequestMethod') is not None:
            self.access_control_request_method = m.get('AccessControlRequestMethod')
        self.addresses = []
        if m.get('Addresses') is not None:
            for k in m.get('Addresses'):
                temp_model = Address()
                self.addresses.append(temp_model.from_map(k))
        if m.get('Album') is not None:
            self.album = m.get('Album')
        if m.get('AlbumArtist') is not None:
            self.album_artist = m.get('AlbumArtist')
        if m.get('Artist') is not None:
            self.artist = m.get('Artist')
        self.audio_covers = []
        if m.get('AudioCovers') is not None:
            for k in m.get('AudioCovers'):
                temp_model = Image()
                self.audio_covers.append(temp_model.from_map(k))
        self.audio_streams = []
        if m.get('AudioStreams') is not None:
            for k in m.get('AudioStreams'):
                temp_model = AudioStream()
                self.audio_streams.append(temp_model.from_map(k))
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('CacheControl') is not None:
            self.cache_control = m.get('CacheControl')
        if m.get('Composer') is not None:
            self.composer = m.get('Composer')
        if m.get('ContentDisposition') is not None:
            self.content_disposition = m.get('ContentDisposition')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('ContentLanguage') is not None:
            self.content_language = m.get('ContentLanguage')
        if m.get('ContentMd5') is not None:
            self.content_md_5 = m.get('ContentMd5')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.cropping_suggestions = []
        if m.get('CroppingSuggestions') is not None:
            for k in m.get('CroppingSuggestions'):
                temp_model = CroppingSuggestion()
                self.cropping_suggestions.append(temp_model.from_map(k))
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('DocumentContent') is not None:
            self.document_content = m.get('DocumentContent')
        if m.get('DocumentLanguage') is not None:
            self.document_language = m.get('DocumentLanguage')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('EXIF') is not None:
            self.exif = m.get('EXIF')
        if m.get('FigureCount') is not None:
            self.figure_count = m.get('FigureCount')
        self.figures = []
        if m.get('Figures') is not None:
            for k in m.get('Figures'):
                temp_model = Figure()
                self.figures.append(temp_model.from_map(k))
        if m.get('FileAccessTime') is not None:
            self.file_access_time = m.get('FileAccessTime')
        if m.get('FileCreateTime') is not None:
            self.file_create_time = m.get('FileCreateTime')
        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')
        if m.get('FileModifiedTime') is not None:
            self.file_modified_time = m.get('FileModifiedTime')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('FormatLongName') is not None:
            self.format_long_name = m.get('FormatLongName')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ImageScore') is not None:
            temp_model = ImageScore()
            self.image_score = temp_model.from_map(m['ImageScore'])
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LatLong') is not None:
            self.lat_long = m.get('LatLong')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        self.ocrcontents = []
        if m.get('OCRContents') is not None:
            for k in m.get('OCRContents'):
                temp_model = OCRContents()
                self.ocrcontents.append(temp_model.from_map(k))
        if m.get('OSSCRC64') is not None:
            self.osscrc64 = m.get('OSSCRC64')
        if m.get('OSSDeleteMarker') is not None:
            self.ossdelete_marker = m.get('OSSDeleteMarker')
        if m.get('OSSExpiration') is not None:
            self.ossexpiration = m.get('OSSExpiration')
        if m.get('OSSObjectType') is not None:
            self.ossobject_type = m.get('OSSObjectType')
        if m.get('OSSStorageClass') is not None:
            self.ossstorage_class = m.get('OSSStorageClass')
        if m.get('OSSTagging') is not None:
            self.osstagging = m.get('OSSTagging')
        if m.get('OSSTaggingCount') is not None:
            self.osstagging_count = m.get('OSSTaggingCount')
        if m.get('OSSURI') is not None:
            self.ossuri = m.get('OSSURI')
        if m.get('OSSUserMeta') is not None:
            self.ossuser_meta = m.get('OSSUserMeta')
        if m.get('OSSVersionId') is not None:
            self.ossversion_id = m.get('OSSVersionId')
        if m.get('ObjectACL') is not None:
            self.object_acl = m.get('ObjectACL')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Orientation') is not None:
            self.orientation = m.get('Orientation')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('Performer') is not None:
            self.performer = m.get('Performer')
        if m.get('ProduceTime') is not None:
            self.produce_time = m.get('ProduceTime')
        if m.get('ProgramCount') is not None:
            self.program_count = m.get('ProgramCount')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ServerSideDataEncryption') is not None:
            self.server_side_data_encryption = m.get('ServerSideDataEncryption')
        if m.get('ServerSideEncryption') is not None:
            self.server_side_encryption = m.get('ServerSideEncryption')
        if m.get('ServerSideEncryptionCustomerAlgorithm') is not None:
            self.server_side_encryption_customer_algorithm = m.get('ServerSideEncryptionCustomerAlgorithm')
        if m.get('ServerSideEncryptionKeyId') is not None:
            self.server_side_encryption_key_id = m.get('ServerSideEncryptionKeyId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamCount') is not None:
            self.stream_count = m.get('StreamCount')
        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k in m.get('Subtitles'):
                temp_model = SubtitleStream()
                self.subtitles.append(temp_model.from_map(k))
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TravelClusterId') is not None:
            self.travel_cluster_id = m.get('TravelClusterId')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VideoHeight') is not None:
            self.video_height = m.get('VideoHeight')
        self.video_streams = []
        if m.get('VideoStreams') is not None:
            for k in m.get('VideoStreams'):
                temp_model = VideoStream()
                self.video_streams.append(temp_model.from_map(k))
        if m.get('VideoWidth') is not None:
            self.video_width = m.get('VideoWidth')
        return self


class FigureCluster(TeaModel):
    def __init__(
        self,
        average_age: float = None,
        cover: File = None,
        create_time: str = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        dataset_name: str = None,
        face_count: int = None,
        gender: str = None,
        image_count: int = None,
        max_age: float = None,
        min_age: float = None,
        name: str = None,
        object_id: str = None,
        object_type: str = None,
        owner_id: str = None,
        project_name: str = None,
        update_time: str = None,
        video_count: int = None,
    ):
        # AverageAge
        self.average_age = average_age
        # Cover
        self.cover = cover
        # CreateTime
        self.create_time = create_time
        # CustomId
        self.custom_id = custom_id
        # CustomLabels
        self.custom_labels = custom_labels
        # DatasetName
        self.dataset_name = dataset_name
        # FaceCount
        self.face_count = face_count
        # Gender
        self.gender = gender
        # ImageCount
        self.image_count = image_count
        # MaxAge
        self.max_age = max_age
        # MinAge
        self.min_age = min_age
        # Name
        self.name = name
        # ObjectId
        self.object_id = object_id
        # ObjectType
        self.object_type = object_type
        # OwnerId
        self.owner_id = owner_id
        # ProjectName
        self.project_name = project_name
        # UpdateTime
        self.update_time = update_time
        # VideoCount
        self.video_count = video_count

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average_age is not None:
            result['AverageAge'] = self.average_age
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.face_count is not None:
            result['FaceCount'] = self.face_count
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.max_age is not None:
            result['MaxAge'] = self.max_age
        if self.min_age is not None:
            result['MinAge'] = self.min_age
        if self.name is not None:
            result['Name'] = self.name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.video_count is not None:
            result['VideoCount'] = self.video_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageAge') is not None:
            self.average_age = m.get('AverageAge')
        if m.get('Cover') is not None:
            temp_model = File()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('MaxAge') is not None:
            self.max_age = m.get('MaxAge')
        if m.get('MinAge') is not None:
            self.min_age = m.get('MinAge')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VideoCount') is not None:
            self.video_count = m.get('VideoCount')
        return self


class FigureClusterForReqCoverFigures(TeaModel):
    def __init__(
        self,
        figure_id: str = None,
    ):
        # FigureId
        self.figure_id = figure_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        return self


class FigureClusterForReqCover(TeaModel):
    def __init__(
        self,
        figures: List[FigureClusterForReqCoverFigures] = None,
    ):
        # Figures
        self.figures = figures

    def validate(self):
        if self.figures:
            for k in self.figures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Figures'] = []
        if self.figures is not None:
            for k in self.figures:
                result['Figures'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.figures = []
        if m.get('Figures') is not None:
            for k in m.get('Figures'):
                temp_model = FigureClusterForReqCoverFigures()
                self.figures.append(temp_model.from_map(k))
        return self


class FigureClusterForReq(TeaModel):
    def __init__(
        self,
        cover: FigureClusterForReqCover = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        name: str = None,
        object_id: str = None,
    ):
        # Cover
        self.cover = cover
        # CustomId
        self.custom_id = custom_id
        # CustomLabels
        self.custom_labels = custom_labels
        # Name
        self.name = name
        # ObjectId
        self.object_id = object_id

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.name is not None:
            result['Name'] = self.name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cover') is not None:
            temp_model = FigureClusterForReqCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        return self


class FileForReqFigures(TeaModel):
    def __init__(
        self,
        figure_cluster_id: str = None,
        figure_id: str = None,
        figure_type: str = None,
    ):
        # FigureClusterId
        self.figure_cluster_id = figure_cluster_id
        # FigureId
        self.figure_id = figure_id
        # FigureType
        self.figure_type = figure_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_cluster_id is not None:
            result['FigureClusterId'] = self.figure_cluster_id
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        if self.figure_type is not None:
            result['FigureType'] = self.figure_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureClusterId') is not None:
            self.figure_cluster_id = m.get('FigureClusterId')
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        if m.get('FigureType') is not None:
            self.figure_type = m.get('FigureType')
        return self


class FileForReq(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        figures: List[FileForReqFigures] = None,
        file_hash: str = None,
        media_type: str = None,
        ossuri: str = None,
        uri: str = None,
    ):
        # ContentType
        self.content_type = content_type
        # CustomId
        self.custom_id = custom_id
        # CustomLabels
        self.custom_labels = custom_labels
        # Figures
        self.figures = figures
        # FileHash
        self.file_hash = file_hash
        # MediaType
        self.media_type = media_type
        # OSSURI
        self.ossuri = ossuri
        # URI
        self.uri = uri

    def validate(self):
        if self.figures:
            for k in self.figures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        result['Figures'] = []
        if self.figures is not None:
            for k in self.figures:
                result['Figures'].append(k.to_map() if k else None)
        if self.file_hash is not None:
            result['FileHash'] = self.file_hash
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.ossuri is not None:
            result['OSSURI'] = self.ossuri
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        self.figures = []
        if m.get('Figures') is not None:
            for k in m.get('Figures'):
                temp_model = FileForReqFigures()
                self.figures.append(temp_model.from_map(k))
        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('OSSURI') is not None:
            self.ossuri = m.get('OSSURI')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class KeyValuePair(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 键
        self.key = key
        # 值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class PresetReference(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # 名称
        self.name = name
        # 类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class Project(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        dataset_count: int = None,
        dataset_max_bind_count: int = None,
        dataset_max_entity_count: int = None,
        dataset_max_file_count: int = None,
        dataset_max_relation_count: int = None,
        dataset_max_total_file_size: int = None,
        description: str = None,
        engine_concurrency: int = None,
        file_count: int = None,
        project_max_dataset_count: int = None,
        project_name: str = None,
        project_queries_per_second: int = None,
        service_role: str = None,
        total_file_size: int = None,
        update_time: str = None,
    ):
        # 创建时间
        self.create_time = create_time
        # 项目当前媒体集数
        self.dataset_count = dataset_count
        # 项目最多绑定数
        self.dataset_max_bind_count = dataset_max_bind_count
        # 项目最多实体数
        self.dataset_max_entity_count = dataset_max_entity_count
        # 项目最多文件数
        self.dataset_max_file_count = dataset_max_file_count
        # 项目最多关系数
        self.dataset_max_relation_count = dataset_max_relation_count
        # 项目最大文件总大小
        self.dataset_max_total_file_size = dataset_max_total_file_size
        # 描述
        self.description = description
        # 项目最大并发数
        self.engine_concurrency = engine_concurrency
        # 项目当前文件数
        self.file_count = file_count
        # 项目最多媒体集数量
        self.project_max_dataset_count = project_max_dataset_count
        # 项目名称
        self.project_name = project_name
        # 项目QPS
        self.project_queries_per_second = project_queries_per_second
        # 服务角色
        self.service_role = service_role
        # 项目当前文件总大小
        self.total_file_size = total_file_size
        # 更新时间
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset_count is not None:
            result['DatasetCount'] = self.dataset_count
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.description is not None:
            result['Description'] = self.description
        if self.engine_concurrency is not None:
            result['EngineConcurrency'] = self.engine_concurrency
        if self.file_count is not None:
            result['FileCount'] = self.file_count
        if self.project_max_dataset_count is not None:
            result['ProjectMaxDatasetCount'] = self.project_max_dataset_count
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_queries_per_second is not None:
            result['ProjectQueriesPerSecond'] = self.project_queries_per_second
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.total_file_size is not None:
            result['TotalFileSize'] = self.total_file_size
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatasetCount') is not None:
            self.dataset_count = m.get('DatasetCount')
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EngineConcurrency') is not None:
            self.engine_concurrency = m.get('EngineConcurrency')
        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')
        if m.get('ProjectMaxDatasetCount') is not None:
            self.project_max_dataset_count = m.get('ProjectMaxDatasetCount')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectQueriesPerSecond') is not None:
            self.project_queries_per_second = m.get('ProjectQueriesPerSecond')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('TotalFileSize') is not None:
            self.total_file_size = m.get('TotalFileSize')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class RegionType(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        # LocalName
        self.local_name = local_name
        # RegionId
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class Row(TeaModel):
    def __init__(
        self,
        custom_labels: List[KeyValuePair] = None,
        uri: str = None,
    ):
        # CustomLabels
        self.custom_labels = custom_labels
        # URI
        self.uri = uri

    def validate(self):
        if self.custom_labels:
            for k in self.custom_labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomLabels'] = []
        if self.custom_labels is not None:
            for k in self.custom_labels:
                result['CustomLabels'].append(k.to_map() if k else None)
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_labels = []
        if m.get('CustomLabels') is not None:
            for k in m.get('CustomLabels'):
                temp_model = KeyValuePair()
                self.custom_labels.append(temp_model.from_map(k))
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class SimpleQuery(TeaModel):
    def __init__(
        self,
        field: str = None,
        operation: str = None,
        sub_queries: List['SimpleQuery'] = None,
        value: str = None,
    ):
        # 需要查询的字段名
        self.field = field
        # 运算符
        self.operation = operation
        # 由 SimpleQuery 结构体组成的子查询数组
        self.sub_queries = sub_queries
        # 需要查询的字段值
        self.value = value

    def validate(self):
        if self.sub_queries:
            for k in self.sub_queries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.operation is not None:
            result['Operation'] = self.operation
        result['SubQueries'] = []
        if self.sub_queries is not None:
            for k in self.sub_queries:
                result['SubQueries'].append(k.to_map() if k else None)
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        self.sub_queries = []
        if m.get('SubQueries') is not None:
            for k in m.get('SubQueries'):
                temp_model = SimpleQuery()
                self.sub_queries.append(temp_model.from_map(k))
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class Story(TeaModel):
    def __init__(
        self,
        cover: File = None,
        create_time: str = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        dataset_name: str = None,
        figure_cluster_ids: List[str] = None,
        files: List[File] = None,
        object_id: str = None,
        object_type: str = None,
        owner_id: str = None,
        project_name: str = None,
        story_end_time: str = None,
        story_name: str = None,
        story_start_time: str = None,
        story_sub_type: str = None,
        story_type: str = None,
        update_time: str = None,
    ):
        self.cover = cover
        # CreateTime
        self.create_time = create_time
        # CustomId
        self.custom_id = custom_id
        # CustomLabels
        self.custom_labels = custom_labels
        # DatasetName
        self.dataset_name = dataset_name
        # FigureClusterIds
        self.figure_cluster_ids = figure_cluster_ids
        # Files
        self.files = files
        # ObjectId
        self.object_id = object_id
        # ObjectType
        self.object_type = object_type
        # OwnerId
        self.owner_id = owner_id
        # ProjectName
        self.project_name = project_name
        # StoryEndTime
        self.story_end_time = story_end_time
        # StoryName
        self.story_name = story_name
        # StoryStartTime
        self.story_start_time = story_start_time
        # StorySubType
        self.story_sub_type = story_sub_type
        # StoryType
        self.story_type = story_type
        # UpdateTime
        self.update_time = update_time

    def validate(self):
        if self.cover:
            self.cover.validate()
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.figure_cluster_ids is not None:
            result['FigureClusterIds'] = self.figure_cluster_ids
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_end_time is not None:
            result['StoryEndTime'] = self.story_end_time
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_start_time is not None:
            result['StoryStartTime'] = self.story_start_time
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cover') is not None:
            temp_model = File()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FigureClusterIds') is not None:
            self.figure_cluster_ids = m.get('FigureClusterIds')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryEndTime') is not None:
            self.story_end_time = m.get('StoryEndTime')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StoryStartTime') is not None:
            self.story_start_time = m.get('StoryStartTime')
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class TaskInfo(TeaModel):
    def __init__(
        self,
        code: str = None,
        end_time: str = None,
        message: str = None,
        start_time: str = None,
        status: str = None,
        tags: Dict[str, Any] = None,
        task_id: str = None,
        task_type: str = None,
        user_data: str = None,
    ):
        # 错误码
        self.code = code
        # 任务结束时间
        self.end_time = end_time
        # 错误消息
        self.message = message
        # 任务开始时间
        self.start_time = start_time
        # 任务状态
        self.status = status
        # 标签
        self.tags = tags
        # 任务唯一ID
        self.task_id = task_id
        # 任务类型
        self.task_type = task_type
        # 用户自定义信息
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.message is not None:
            result['Message'] = self.message
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class TimeRange(TeaModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        # end time
        self.end = end
        # start time
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class TrimPolicy(TeaModel):
    def __init__(
        self,
        disable_delete_empty_cell: bool = None,
        disable_delete_repeated_style: bool = None,
        disable_delete_unused_picture: bool = None,
        disable_delete_unused_shape: bool = None,
    ):
        # 禁止删除所有空单元格
        self.disable_delete_empty_cell = disable_delete_empty_cell
        # 禁止删除所有重复样式
        self.disable_delete_repeated_style = disable_delete_repeated_style
        # 禁止删除未使用的单元格图片
        self.disable_delete_unused_picture = disable_delete_unused_picture
        # 禁止删除没有使用的Shape
        self.disable_delete_unused_shape = disable_delete_unused_shape

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable_delete_empty_cell is not None:
            result['DisableDeleteEmptyCell'] = self.disable_delete_empty_cell
        if self.disable_delete_repeated_style is not None:
            result['DisableDeleteRepeatedStyle'] = self.disable_delete_repeated_style
        if self.disable_delete_unused_picture is not None:
            result['DisableDeleteUnusedPicture'] = self.disable_delete_unused_picture
        if self.disable_delete_unused_shape is not None:
            result['DisableDeleteUnusedShape'] = self.disable_delete_unused_shape
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableDeleteEmptyCell') is not None:
            self.disable_delete_empty_cell = m.get('DisableDeleteEmptyCell')
        if m.get('DisableDeleteRepeatedStyle') is not None:
            self.disable_delete_repeated_style = m.get('DisableDeleteRepeatedStyle')
        if m.get('DisableDeleteUnusedPicture') is not None:
            self.disable_delete_unused_picture = m.get('DisableDeleteUnusedPicture')
        if m.get('DisableDeleteUnusedShape') is not None:
            self.disable_delete_unused_shape = m.get('DisableDeleteUnusedShape')
        return self


class WebofficePermission(TeaModel):
    def __init__(
        self,
        copy: bool = None,
        export: bool = None,
        history: bool = None,
        print: bool = None,
        readonly: bool = None,
        rename: bool = None,
    ):
        # 拷贝
        self.copy = copy
        # 导出
        self.export = export
        # 查看历史版本
        self.history = history
        # 打印
        self.print = print
        # 只读模式
        self.readonly = readonly
        # 重命名
        self.rename = rename

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.copy is not None:
            result['Copy'] = self.copy
        if self.export is not None:
            result['Export'] = self.export
        if self.history is not None:
            result['History'] = self.history
        if self.print is not None:
            result['Print'] = self.print
        if self.readonly is not None:
            result['Readonly'] = self.readonly
        if self.rename is not None:
            result['Rename'] = self.rename
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Copy') is not None:
            self.copy = m.get('Copy')
        if m.get('Export') is not None:
            self.export = m.get('Export')
        if m.get('History') is not None:
            self.history = m.get('History')
        if m.get('Print') is not None:
            self.print = m.get('Print')
        if m.get('Readonly') is not None:
            self.readonly = m.get('Readonly')
        if m.get('Rename') is not None:
            self.rename = m.get('Rename')
        return self


class WebofficeUser(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        id: str = None,
        name: str = None,
    ):
        # 头像
        self.avatar = avatar
        # Id
        self.id = id
        # 名字
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class WebofficeWatermark(TeaModel):
    def __init__(
        self,
        fill_style: str = None,
        font: str = None,
        horizontal: int = None,
        rotate: float = None,
        type: int = None,
        value: str = None,
        vertical: int = None,
    ):
        # 字体颜色
        self.fill_style = fill_style
        # 字体样式
        self.font = font
        # 水平间距
        self.horizontal = horizontal
        # 旋转角度
        self.rotate = rotate
        # 水印类型，目前仅支持文字水印，0: 无水印；1: 文字水印
        self.type = type
        # 水印文字
        self.value = value
        # 垂直间距
        self.vertical = vertical

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fill_style is not None:
            result['FillStyle'] = self.fill_style
        if self.font is not None:
            result['Font'] = self.font
        if self.horizontal is not None:
            result['Horizontal'] = self.horizontal
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.vertical is not None:
            result['Vertical'] = self.vertical
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FillStyle') is not None:
            self.fill_style = m.get('FillStyle')
        if m.get('Font') is not None:
            self.font = m.get('Font')
        if m.get('Horizontal') is not None:
            self.horizontal = m.get('Horizontal')
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')
        return self


class AddStoryFilesRequestFiles(TeaModel):
    def __init__(
        self,
        uri: str = None,
    ):
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class AddStoryFilesRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        files: List[AddStoryFilesRequestFiles] = None,
        object_id: str = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.files = files
        self.object_id = object_id
        # A short description of struct
        self.project_name = project_name

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = AddStoryFilesRequestFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class AddStoryFilesShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        files_shrink: str = None,
        object_id: str = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.files_shrink = files_shrink
        self.object_id = object_id
        # A short description of struct
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class AddStoryFilesResponseBodyFiles(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        uri: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class AddStoryFilesResponseBody(TeaModel):
    def __init__(
        self,
        files: List[AddStoryFilesResponseBodyFiles] = None,
        request_id: str = None,
    ):
        self.files = files
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = AddStoryFilesResponseBodyFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddStoryFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddStoryFilesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AddStoryFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachOSSBucketRequest(TeaModel):
    def __init__(
        self,
        ossbucket: str = None,
        project_name: str = None,
    ):
        self.ossbucket = ossbucket
        # 项目名称
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class AttachOSSBucketResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # RequestId
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachOSSBucketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachOSSBucketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AttachOSSBucketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uris: List[str] = None,
    ):
        self.dataset_name = dataset_name
        self.project_name = project_name
        self.uris = uris

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uris is not None:
            result['URIs'] = self.uris
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URIs') is not None:
            self.uris = m.get('URIs')
        return self


class BatchDeleteFileMetaShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uris_shrink: str = None,
    ):
        self.dataset_name = dataset_name
        self.project_name = project_name
        self.uris_shrink = uris_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uris_shrink is not None:
            result['URIs'] = self.uris_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URIs') is not None:
            self.uris_shrink = m.get('URIs')
        return self


class BatchDeleteFileMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchDeleteFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchDeleteFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = BatchDeleteFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGetFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uris: List[str] = None,
    ):
        self.dataset_name = dataset_name
        self.project_name = project_name
        self.uris = uris

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uris is not None:
            result['URIs'] = self.uris
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URIs') is not None:
            self.uris = m.get('URIs')
        return self


class BatchGetFileMetaShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uris_shrink: str = None,
    ):
        self.dataset_name = dataset_name
        self.project_name = project_name
        self.uris_shrink = uris_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uris_shrink is not None:
            result['URIs'] = self.uris_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URIs') is not None:
            self.uris_shrink = m.get('URIs')
        return self


class BatchGetFileMetaResponseBody(TeaModel):
    def __init__(
        self,
        files: List[File] = None,
        request_id: str = None,
    ):
        self.files = files
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchGetFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchGetFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = BatchGetFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchIndexFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        files: List[FileForReq] = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.files = files
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.project_name = project_name

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = FileForReq()
                self.files.append(temp_model.from_map(k))
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class BatchIndexFileMetaShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        files_shrink: str = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.files_shrink = files_shrink
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class BatchIndexFileMetaResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
    ):
        self.event_id = event_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchIndexFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchIndexFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = BatchIndexFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUpdateFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        files: List[FileForReq] = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.files = files
        self.project_name = project_name

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = FileForReq()
                self.files.append(temp_model.from_map(k))
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class BatchUpdateFileMetaShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        files_shrink: str = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.files_shrink = files_shrink
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class BatchUpdateFileMetaResponseBodyFiles(TeaModel):
    def __init__(
        self,
        message: str = None,
        success: bool = None,
        uri: str = None,
    ):
        self.message = message
        self.success = success
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class BatchUpdateFileMetaResponseBody(TeaModel):
    def __init__(
        self,
        files: List[BatchUpdateFileMetaResponseBodyFiles] = None,
        request_id: str = None,
    ):
        self.files = files
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = BatchUpdateFileMetaResponseBodyFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchUpdateFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchUpdateFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = BatchUpdateFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBindingRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uri: str = None,
    ):
        # DatasetName
        self.dataset_name = dataset_name
        # ProjectName
        self.project_name = project_name
        # URI
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateBindingResponseBody(TeaModel):
    def __init__(
        self,
        binding: Binding = None,
        request_id: str = None,
    ):
        self.binding = binding
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.binding:
            self.binding.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binding is not None:
            result['Binding'] = self.binding.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Binding') is not None:
            temp_model = Binding()
            self.binding = temp_model.from_map(m['Binding'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBindingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBindingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatasetRequest(TeaModel):
    def __init__(
        self,
        dataset_max_bind_count: int = None,
        dataset_max_entity_count: int = None,
        dataset_max_file_count: int = None,
        dataset_max_relation_count: int = None,
        dataset_max_total_file_size: int = None,
        dataset_name: str = None,
        description: str = None,
        project_name: str = None,
        template_id: str = None,
    ):
        # 媒体集最多帮定数
        self.dataset_max_bind_count = dataset_max_bind_count
        # 媒体集最多实体数
        self.dataset_max_entity_count = dataset_max_entity_count
        # 媒体集最多文件数
        self.dataset_max_file_count = dataset_max_file_count
        # 媒体集最多关系数
        self.dataset_max_relation_count = dataset_max_relation_count
        # 媒体集最大文件总大小
        self.dataset_max_total_file_size = dataset_max_total_file_size
        # 数据集名称
        self.dataset_name = dataset_name
        # 对数据集的描述
        self.description = description
        # 项目名称
        self.project_name = project_name
        # 模板Id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateDatasetResponseBody(TeaModel):
    def __init__(
        self,
        dataset: Dataset = None,
        request_id: str = None,
    ):
        self.dataset = dataset
        # 请求 ID
        self.request_id = request_id

    def validate(self):
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dataset') is not None:
            temp_model = Dataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDatasetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDetectVideoLabelsTaskRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
        source_uri: str = None,
        tags: Dict[str, Any] = None,
        user_data: str = None,
    ):
        self.credential_config = credential_config
        # NotifyEndpoint
        self.notify_endpoint = notify_endpoint
        # NotifyTopicName
        self.notify_topic_name = notify_topic_name
        # 项目名称
        self.project_name = project_name
        # SourceURI
        self.source_uri = source_uri
        self.tags = tags
        # UserData
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateDetectVideoLabelsTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
        source_uri: str = None,
        tags_shrink: str = None,
        user_data: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        # NotifyEndpoint
        self.notify_endpoint = notify_endpoint
        # NotifyTopicName
        self.notify_topic_name = notify_topic_name
        # 项目名称
        self.project_name = project_name
        # SourceURI
        self.source_uri = source_uri
        self.tags_shrink = tags_shrink
        # UserData
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateDetectVideoLabelsTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # 事件Id
        self.event_id = event_id
        # 请求唯一Id
        self.request_id = request_id
        # 任务唯一ID
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateDetectVideoLabelsTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDetectVideoLabelsTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateDetectVideoLabelsTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFigureClusteringTaskRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
        tags: Dict[str, Any] = None,
        user_data: str = None,
    ):
        self.dataset_name = dataset_name
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.project_name = project_name
        self.tags = tags
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFigureClusteringTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
        tags_shrink: str = None,
        user_data: str = None,
    ):
        self.dataset_name = dataset_name
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.project_name = project_name
        self.tags_shrink = tags_shrink
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFigureClusteringTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        # Id of the request
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateFigureClusteringTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFigureClusteringTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateFigureClusteringTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFigureClustersMergingTaskRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        from_: str = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
        tags: Dict[str, Any] = None,
        to: str = None,
        user_data: str = None,
    ):
        self.dataset_name = dataset_name
        # 源cluster
        self.from_ = from_
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.project_name = project_name
        self.tags = tags
        # 目的cluster
        self.to = to
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.from_ is not None:
            result['From'] = self.from_
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.to is not None:
            result['To'] = self.to
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFigureClustersMergingTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        from_: str = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
        tags_shrink: str = None,
        to: str = None,
        user_data: str = None,
    ):
        self.dataset_name = dataset_name
        # 源cluster
        self.from_ = from_
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.project_name = project_name
        self.tags_shrink = tags_shrink
        # 目的cluster
        self.to = to
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.from_ is not None:
            result['From'] = self.from_
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.to is not None:
            result['To'] = self.to
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFigureClustersMergingTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        # Id of the request
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateFigureClustersMergingTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFigureClustersMergingTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateFigureClustersMergingTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageModerationTaskRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        interval: int = None,
        max_frames: int = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
        reviewer: str = None,
        scenes: List[str] = None,
        source_uri: str = None,
        tags: Dict[str, Any] = None,
        user_data: str = None,
    ):
        self.credential_config = credential_config
        self.interval = interval
        self.max_frames = max_frames
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        # 项目名称
        self.project_name = project_name
        self.reviewer = reviewer
        self.scenes = scenes
        self.source_uri = source_uri
        self.tags = tags
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.max_frames is not None:
            result['MaxFrames'] = self.max_frames
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.reviewer is not None:
            result['Reviewer'] = self.reviewer
        if self.scenes is not None:
            result['Scenes'] = self.scenes
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('MaxFrames') is not None:
            self.max_frames = m.get('MaxFrames')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Reviewer') is not None:
            self.reviewer = m.get('Reviewer')
        if m.get('Scenes') is not None:
            self.scenes = m.get('Scenes')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateImageModerationTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        interval: int = None,
        max_frames: int = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
        reviewer: str = None,
        scenes_shrink: str = None,
        source_uri: str = None,
        tags_shrink: str = None,
        user_data: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        self.interval = interval
        self.max_frames = max_frames
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        # 项目名称
        self.project_name = project_name
        self.reviewer = reviewer
        self.scenes_shrink = scenes_shrink
        self.source_uri = source_uri
        self.tags_shrink = tags_shrink
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.max_frames is not None:
            result['MaxFrames'] = self.max_frames
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.reviewer is not None:
            result['Reviewer'] = self.reviewer
        if self.scenes_shrink is not None:
            result['Scenes'] = self.scenes_shrink
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('MaxFrames') is not None:
            self.max_frames = m.get('MaxFrames')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Reviewer') is not None:
            self.reviewer = m.get('Reviewer')
        if m.get('Scenes') is not None:
            self.scenes_shrink = m.get('Scenes')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateImageModerationTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        # RequestId
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateImageModerationTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateImageModerationTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateImageModerationTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageSplicingTaskRequestSources(TeaModel):
    def __init__(
        self,
        rotate: int = None,
        uri: str = None,
    ):
        self.rotate = rotate
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateImageSplicingTaskRequest(TeaModel):
    def __init__(
        self,
        align: int = None,
        background_color: str = None,
        credential_config: CredentialConfig = None,
        direction: str = None,
        image_format: str = None,
        margin: int = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        padding: int = None,
        project_name: str = None,
        quality: int = None,
        scale_type: str = None,
        sources: List[CreateImageSplicingTaskRequestSources] = None,
        tags: Dict[str, Any] = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        self.align = align
        self.background_color = background_color
        self.credential_config = credential_config
        self.direction = direction
        self.image_format = image_format
        self.margin = margin
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.padding = padding
        # A short description of struct
        self.project_name = project_name
        self.quality = quality
        self.scale_type = scale_type
        self.sources = sources
        self.tags = tags
        self.target_uri = target_uri
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.sources:
            for k in self.sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.align is not None:
            result['Align'] = self.align
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.margin is not None:
            result['Margin'] = self.margin
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.padding is not None:
            result['Padding'] = self.padding
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        result['Sources'] = []
        if self.sources is not None:
            for k in self.sources:
                result['Sources'].append(k.to_map() if k else None)
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Align') is not None:
            self.align = m.get('Align')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('Margin') is not None:
            self.margin = m.get('Margin')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('Padding') is not None:
            self.padding = m.get('Padding')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        self.sources = []
        if m.get('Sources') is not None:
            for k in m.get('Sources'):
                temp_model = CreateImageSplicingTaskRequestSources()
                self.sources.append(temp_model.from_map(k))
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateImageSplicingTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        align: int = None,
        background_color: str = None,
        credential_config_shrink: str = None,
        direction: str = None,
        image_format: str = None,
        margin: int = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        padding: int = None,
        project_name: str = None,
        quality: int = None,
        scale_type: str = None,
        sources_shrink: str = None,
        tags_shrink: str = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        self.align = align
        self.background_color = background_color
        self.credential_config_shrink = credential_config_shrink
        self.direction = direction
        self.image_format = image_format
        self.margin = margin
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.padding = padding
        # A short description of struct
        self.project_name = project_name
        self.quality = quality
        self.scale_type = scale_type
        self.sources_shrink = sources_shrink
        self.tags_shrink = tags_shrink
        self.target_uri = target_uri
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.align is not None:
            result['Align'] = self.align
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.margin is not None:
            result['Margin'] = self.margin
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.padding is not None:
            result['Padding'] = self.padding
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Align') is not None:
            self.align = m.get('Align')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('Margin') is not None:
            self.margin = m.get('Margin')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('Padding') is not None:
            self.padding = m.get('Padding')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateImageSplicingTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateImageSplicingTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateImageSplicingTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateImageSplicingTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMediaConvertTaskRequestSourcesSubtitles(TeaModel):
    def __init__(
        self,
        language: str = None,
        time_offset: float = None,
        uri: str = None,
    ):
        self.language = language
        self.time_offset = time_offset
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.time_offset is not None:
            result['TimeOffset'] = self.time_offset
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('TimeOffset') is not None:
            self.time_offset = m.get('TimeOffset')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateMediaConvertTaskRequestSources(TeaModel):
    def __init__(
        self,
        duration: float = None,
        start_time: float = None,
        subtitles: List[CreateMediaConvertTaskRequestSourcesSubtitles] = None,
        uri: str = None,
    ):
        self.duration = duration
        self.start_time = start_time
        self.subtitles = subtitles
        self.uri = uri

    def validate(self):
        if self.subtitles:
            for k in self.subtitles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        result['Subtitles'] = []
        if self.subtitles is not None:
            for k in self.subtitles:
                result['Subtitles'].append(k.to_map() if k else None)
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k in m.get('Subtitles'):
                temp_model = CreateMediaConvertTaskRequestSourcesSubtitles()
                self.subtitles.append(temp_model.from_map(k))
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateMediaConvertTaskRequestTargetsAudioFilterAudio(TeaModel):
    def __init__(
        self,
        mixing: bool = None,
    ):
        self.mixing = mixing

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mixing is not None:
            result['Mixing'] = self.mixing
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mixing') is not None:
            self.mixing = m.get('Mixing')
        return self


class CreateMediaConvertTaskRequestTargetsAudioTranscodeAudio(TeaModel):
    def __init__(
        self,
        bitrate: int = None,
        bitrate_option: str = None,
        channel: int = None,
        codec: str = None,
        quality: int = None,
        sample_rate: int = None,
        sample_rate_option: str = None,
    ):
        self.bitrate = bitrate
        self.bitrate_option = bitrate_option
        self.channel = channel
        self.codec = codec
        self.quality = quality
        self.sample_rate = sample_rate
        self.sample_rate_option = sample_rate_option

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.bitrate_option is not None:
            result['BitrateOption'] = self.bitrate_option
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.codec is not None:
            result['Codec'] = self.codec
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.sample_rate_option is not None:
            result['SampleRateOption'] = self.sample_rate_option
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('BitrateOption') is not None:
            self.bitrate_option = m.get('BitrateOption')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Codec') is not None:
            self.codec = m.get('Codec')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SampleRateOption') is not None:
            self.sample_rate_option = m.get('SampleRateOption')
        return self


class CreateMediaConvertTaskRequestTargetsAudio(TeaModel):
    def __init__(
        self,
        disable_audio: bool = None,
        filter_audio: CreateMediaConvertTaskRequestTargetsAudioFilterAudio = None,
        transcode_audio: CreateMediaConvertTaskRequestTargetsAudioTranscodeAudio = None,
    ):
        self.disable_audio = disable_audio
        self.filter_audio = filter_audio
        self.transcode_audio = transcode_audio

    def validate(self):
        if self.filter_audio:
            self.filter_audio.validate()
        if self.transcode_audio:
            self.transcode_audio.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable_audio is not None:
            result['DisableAudio'] = self.disable_audio
        if self.filter_audio is not None:
            result['FilterAudio'] = self.filter_audio.to_map()
        if self.transcode_audio is not None:
            result['TranscodeAudio'] = self.transcode_audio.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableAudio') is not None:
            self.disable_audio = m.get('DisableAudio')
        if m.get('FilterAudio') is not None:
            temp_model = CreateMediaConvertTaskRequestTargetsAudioFilterAudio()
            self.filter_audio = temp_model.from_map(m['FilterAudio'])
        if m.get('TranscodeAudio') is not None:
            temp_model = CreateMediaConvertTaskRequestTargetsAudioTranscodeAudio()
            self.transcode_audio = temp_model.from_map(m['TranscodeAudio'])
        return self


class CreateMediaConvertTaskRequestTargetsImageSnapshots(TeaModel):
    def __init__(
        self,
        format: str = None,
        height: int = None,
        interval: float = None,
        number: int = None,
        scale_type: str = None,
        start_time: float = None,
        uri: str = None,
        width: int = None,
    ):
        self.format = format
        self.height = height
        self.interval = interval
        self.number = number
        self.scale_type = scale_type
        self.start_time = start_time
        self.uri = uri
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.height is not None:
            result['Height'] = self.height
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.number is not None:
            result['Number'] = self.number
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uri is not None:
            result['URI'] = self.uri
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class CreateMediaConvertTaskRequestTargetsImageSprites(TeaModel):
    def __init__(
        self,
        format: str = None,
        interval: float = None,
        margin: int = None,
        number: int = None,
        pad: int = None,
        scale_height: float = None,
        scale_type: str = None,
        scale_width: float = None,
        start_time: float = None,
        tile_height: int = None,
        tile_width: int = None,
        uri: str = None,
    ):
        self.format = format
        self.interval = interval
        self.margin = margin
        self.number = number
        self.pad = pad
        self.scale_height = scale_height
        self.scale_type = scale_type
        self.scale_width = scale_width
        self.start_time = start_time
        self.tile_height = tile_height
        self.tile_width = tile_width
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.margin is not None:
            result['Margin'] = self.margin
        if self.number is not None:
            result['Number'] = self.number
        if self.pad is not None:
            result['Pad'] = self.pad
        if self.scale_height is not None:
            result['ScaleHeight'] = self.scale_height
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        if self.scale_width is not None:
            result['ScaleWidth'] = self.scale_width
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tile_height is not None:
            result['TileHeight'] = self.tile_height
        if self.tile_width is not None:
            result['TileWidth'] = self.tile_width
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Margin') is not None:
            self.margin = m.get('Margin')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Pad') is not None:
            self.pad = m.get('Pad')
        if m.get('ScaleHeight') is not None:
            self.scale_height = m.get('ScaleHeight')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        if m.get('ScaleWidth') is not None:
            self.scale_width = m.get('ScaleWidth')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TileHeight') is not None:
            self.tile_height = m.get('TileHeight')
        if m.get('TileWidth') is not None:
            self.tile_width = m.get('TileWidth')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateMediaConvertTaskRequestTargetsImage(TeaModel):
    def __init__(
        self,
        snapshots: List[CreateMediaConvertTaskRequestTargetsImageSnapshots] = None,
        sprites: List[CreateMediaConvertTaskRequestTargetsImageSprites] = None,
    ):
        self.snapshots = snapshots
        self.sprites = sprites

    def validate(self):
        if self.snapshots:
            for k in self.snapshots:
                if k:
                    k.validate()
        if self.sprites:
            for k in self.sprites:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        result['Sprites'] = []
        if self.sprites is not None:
            for k in self.sprites:
                result['Sprites'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = CreateMediaConvertTaskRequestTargetsImageSnapshots()
                self.snapshots.append(temp_model.from_map(k))
        self.sprites = []
        if m.get('Sprites') is not None:
            for k in m.get('Sprites'):
                temp_model = CreateMediaConvertTaskRequestTargetsImageSprites()
                self.sprites.append(temp_model.from_map(k))
        return self


class CreateMediaConvertTaskRequestTargetsSegment(TeaModel):
    def __init__(
        self,
        duration: float = None,
        format: str = None,
        start_number: int = None,
    ):
        self.duration = duration
        self.format = format
        self.start_number = start_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.format is not None:
            result['Format'] = self.format
        if self.start_number is not None:
            result['StartNumber'] = self.start_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('StartNumber') is not None:
            self.start_number = m.get('StartNumber')
        return self


class CreateMediaConvertTaskRequestTargetsSubtitleExtractSubtitle(TeaModel):
    def __init__(
        self,
        format: str = None,
        uri: str = None,
    ):
        self.format = format
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateMediaConvertTaskRequestTargetsSubtitle(TeaModel):
    def __init__(
        self,
        disable_subtitle: bool = None,
        extract_subtitle: CreateMediaConvertTaskRequestTargetsSubtitleExtractSubtitle = None,
    ):
        self.disable_subtitle = disable_subtitle
        self.extract_subtitle = extract_subtitle

    def validate(self):
        if self.extract_subtitle:
            self.extract_subtitle.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable_subtitle is not None:
            result['DisableSubtitle'] = self.disable_subtitle
        if self.extract_subtitle is not None:
            result['ExtractSubtitle'] = self.extract_subtitle.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableSubtitle') is not None:
            self.disable_subtitle = m.get('DisableSubtitle')
        if m.get('ExtractSubtitle') is not None:
            temp_model = CreateMediaConvertTaskRequestTargetsSubtitleExtractSubtitle()
            self.extract_subtitle = temp_model.from_map(m['ExtractSubtitle'])
        return self


class CreateMediaConvertTaskRequestTargetsVideoFilterVideoDelogos(TeaModel):
    def __init__(
        self,
        duration: float = None,
        dx: float = None,
        dy: float = None,
        height: float = None,
        refer_pos: str = None,
        start_time: float = None,
        width: float = None,
    ):
        self.duration = duration
        self.dx = dx
        self.dy = dy
        self.height = height
        self.refer_pos = refer_pos
        self.start_time = start_time
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.dx is not None:
            result['Dx'] = self.dx
        if self.dy is not None:
            result['Dy'] = self.dy
        if self.height is not None:
            result['Height'] = self.height
        if self.refer_pos is not None:
            result['ReferPos'] = self.refer_pos
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Dx') is not None:
            self.dx = m.get('Dx')
        if m.get('Dy') is not None:
            self.dy = m.get('Dy')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class CreateMediaConvertTaskRequestTargetsVideoFilterVideoWatermarks(TeaModel):
    def __init__(
        self,
        border_color: str = None,
        border_width: int = None,
        content: str = None,
        duration: float = None,
        dx: float = None,
        dy: float = None,
        font_apha: float = None,
        font_color: str = None,
        font_name: str = None,
        font_size: int = None,
        height: float = None,
        refer_pos: str = None,
        start_time: float = None,
        type: str = None,
        uri: str = None,
        width: float = None,
    ):
        self.border_color = border_color
        self.border_width = border_width
        self.content = content
        self.duration = duration
        self.dx = dx
        self.dy = dy
        self.font_apha = font_apha
        self.font_color = font_color
        self.font_name = font_name
        self.font_size = font_size
        self.height = height
        self.refer_pos = refer_pos
        self.start_time = start_time
        self.type = type
        self.uri = uri
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.border_color is not None:
            result['BorderColor'] = self.border_color
        if self.border_width is not None:
            result['BorderWidth'] = self.border_width
        if self.content is not None:
            result['Content'] = self.content
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.dx is not None:
            result['Dx'] = self.dx
        if self.dy is not None:
            result['Dy'] = self.dy
        if self.font_apha is not None:
            result['FontApha'] = self.font_apha
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_name is not None:
            result['FontName'] = self.font_name
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.height is not None:
            result['Height'] = self.height
        if self.refer_pos is not None:
            result['ReferPos'] = self.refer_pos
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['URI'] = self.uri
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BorderColor') is not None:
            self.border_color = m.get('BorderColor')
        if m.get('BorderWidth') is not None:
            self.border_width = m.get('BorderWidth')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Dx') is not None:
            self.dx = m.get('Dx')
        if m.get('Dy') is not None:
            self.dy = m.get('Dy')
        if m.get('FontApha') is not None:
            self.font_apha = m.get('FontApha')
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontName') is not None:
            self.font_name = m.get('FontName')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class CreateMediaConvertTaskRequestTargetsVideoFilterVideo(TeaModel):
    def __init__(
        self,
        delogos: List[CreateMediaConvertTaskRequestTargetsVideoFilterVideoDelogos] = None,
        watermarks: List[CreateMediaConvertTaskRequestTargetsVideoFilterVideoWatermarks] = None,
    ):
        self.delogos = delogos
        self.watermarks = watermarks

    def validate(self):
        if self.delogos:
            for k in self.delogos:
                if k:
                    k.validate()
        if self.watermarks:
            for k in self.watermarks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Delogos'] = []
        if self.delogos is not None:
            for k in self.delogos:
                result['Delogos'].append(k.to_map() if k else None)
        result['Watermarks'] = []
        if self.watermarks is not None:
            for k in self.watermarks:
                result['Watermarks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delogos = []
        if m.get('Delogos') is not None:
            for k in m.get('Delogos'):
                temp_model = CreateMediaConvertTaskRequestTargetsVideoFilterVideoDelogos()
                self.delogos.append(temp_model.from_map(k))
        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k in m.get('Watermarks'):
                temp_model = CreateMediaConvertTaskRequestTargetsVideoFilterVideoWatermarks()
                self.watermarks.append(temp_model.from_map(k))
        return self


class CreateMediaConvertTaskRequestTargetsVideoTranscodeVideo(TeaModel):
    def __init__(
        self,
        adaptive_resolution_direction: bool = None,
        bframes: int = None,
        bitrate: int = None,
        bitrate_option: str = None,
        buffer_size: int = None,
        crf: float = None,
        codec: str = None,
        frame_rate: float = None,
        frame_rate_option: str = None,
        gopsize: int = None,
        max_bitrate: int = None,
        pixel_format: str = None,
        refs: int = None,
        resolution: str = None,
        resolution_option: str = None,
        rotation: int = None,
        scale_type: str = None,
    ):
        self.adaptive_resolution_direction = adaptive_resolution_direction
        self.bframes = bframes
        self.bitrate = bitrate
        self.bitrate_option = bitrate_option
        self.buffer_size = buffer_size
        self.crf = crf
        self.codec = codec
        self.frame_rate = frame_rate
        self.frame_rate_option = frame_rate_option
        self.gopsize = gopsize
        self.max_bitrate = max_bitrate
        self.pixel_format = pixel_format
        self.refs = refs
        self.resolution = resolution
        self.resolution_option = resolution_option
        self.rotation = rotation
        self.scale_type = scale_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adaptive_resolution_direction is not None:
            result['AdaptiveResolutionDirection'] = self.adaptive_resolution_direction
        if self.bframes is not None:
            result['BFrames'] = self.bframes
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.bitrate_option is not None:
            result['BitrateOption'] = self.bitrate_option
        if self.buffer_size is not None:
            result['BufferSize'] = self.buffer_size
        if self.crf is not None:
            result['CRF'] = self.crf
        if self.codec is not None:
            result['Codec'] = self.codec
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.frame_rate_option is not None:
            result['FrameRateOption'] = self.frame_rate_option
        if self.gopsize is not None:
            result['GOPSize'] = self.gopsize
        if self.max_bitrate is not None:
            result['MaxBitrate'] = self.max_bitrate
        if self.pixel_format is not None:
            result['PixelFormat'] = self.pixel_format
        if self.refs is not None:
            result['Refs'] = self.refs
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.resolution_option is not None:
            result['ResolutionOption'] = self.resolution_option
        if self.rotation is not None:
            result['Rotation'] = self.rotation
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptiveResolutionDirection') is not None:
            self.adaptive_resolution_direction = m.get('AdaptiveResolutionDirection')
        if m.get('BFrames') is not None:
            self.bframes = m.get('BFrames')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('BitrateOption') is not None:
            self.bitrate_option = m.get('BitrateOption')
        if m.get('BufferSize') is not None:
            self.buffer_size = m.get('BufferSize')
        if m.get('CRF') is not None:
            self.crf = m.get('CRF')
        if m.get('Codec') is not None:
            self.codec = m.get('Codec')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('FrameRateOption') is not None:
            self.frame_rate_option = m.get('FrameRateOption')
        if m.get('GOPSize') is not None:
            self.gopsize = m.get('GOPSize')
        if m.get('MaxBitrate') is not None:
            self.max_bitrate = m.get('MaxBitrate')
        if m.get('PixelFormat') is not None:
            self.pixel_format = m.get('PixelFormat')
        if m.get('Refs') is not None:
            self.refs = m.get('Refs')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('ResolutionOption') is not None:
            self.resolution_option = m.get('ResolutionOption')
        if m.get('Rotation') is not None:
            self.rotation = m.get('Rotation')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        return self


class CreateMediaConvertTaskRequestTargetsVideo(TeaModel):
    def __init__(
        self,
        disable_video: bool = None,
        filter_video: CreateMediaConvertTaskRequestTargetsVideoFilterVideo = None,
        transcode_video: CreateMediaConvertTaskRequestTargetsVideoTranscodeVideo = None,
    ):
        self.disable_video = disable_video
        self.filter_video = filter_video
        self.transcode_video = transcode_video

    def validate(self):
        if self.filter_video:
            self.filter_video.validate()
        if self.transcode_video:
            self.transcode_video.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable_video is not None:
            result['DisableVideo'] = self.disable_video
        if self.filter_video is not None:
            result['FilterVideo'] = self.filter_video.to_map()
        if self.transcode_video is not None:
            result['TranscodeVideo'] = self.transcode_video.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableVideo') is not None:
            self.disable_video = m.get('DisableVideo')
        if m.get('FilterVideo') is not None:
            temp_model = CreateMediaConvertTaskRequestTargetsVideoFilterVideo()
            self.filter_video = temp_model.from_map(m['FilterVideo'])
        if m.get('TranscodeVideo') is not None:
            temp_model = CreateMediaConvertTaskRequestTargetsVideoTranscodeVideo()
            self.transcode_video = temp_model.from_map(m['TranscodeVideo'])
        return self


class CreateMediaConvertTaskRequestTargets(TeaModel):
    def __init__(
        self,
        audio: CreateMediaConvertTaskRequestTargetsAudio = None,
        container: str = None,
        image: CreateMediaConvertTaskRequestTargetsImage = None,
        preset: PresetReference = None,
        segment: CreateMediaConvertTaskRequestTargetsSegment = None,
        speed: float = None,
        subtitle: CreateMediaConvertTaskRequestTargetsSubtitle = None,
        uri: str = None,
        video: CreateMediaConvertTaskRequestTargetsVideo = None,
    ):
        self.audio = audio
        self.container = container
        self.image = image
        self.preset = preset
        self.segment = segment
        self.speed = speed
        self.subtitle = subtitle
        self.uri = uri
        self.video = video

    def validate(self):
        if self.audio:
            self.audio.validate()
        if self.image:
            self.image.validate()
        if self.preset:
            self.preset.validate()
        if self.segment:
            self.segment.validate()
        if self.subtitle:
            self.subtitle.validate()
        if self.video:
            self.video.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio is not None:
            result['Audio'] = self.audio.to_map()
        if self.container is not None:
            result['Container'] = self.container
        if self.image is not None:
            result['Image'] = self.image.to_map()
        if self.preset is not None:
            result['Preset'] = self.preset.to_map()
        if self.segment is not None:
            result['Segment'] = self.segment.to_map()
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.subtitle is not None:
            result['Subtitle'] = self.subtitle.to_map()
        if self.uri is not None:
            result['URI'] = self.uri
        if self.video is not None:
            result['Video'] = self.video.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audio') is not None:
            temp_model = CreateMediaConvertTaskRequestTargetsAudio()
            self.audio = temp_model.from_map(m['Audio'])
        if m.get('Container') is not None:
            self.container = m.get('Container')
        if m.get('Image') is not None:
            temp_model = CreateMediaConvertTaskRequestTargetsImage()
            self.image = temp_model.from_map(m['Image'])
        if m.get('Preset') is not None:
            temp_model = PresetReference()
            self.preset = temp_model.from_map(m['Preset'])
        if m.get('Segment') is not None:
            temp_model = CreateMediaConvertTaskRequestTargetsSegment()
            self.segment = temp_model.from_map(m['Segment'])
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('Subtitle') is not None:
            temp_model = CreateMediaConvertTaskRequestTargetsSubtitle()
            self.subtitle = temp_model.from_map(m['Subtitle'])
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('Video') is not None:
            temp_model = CreateMediaConvertTaskRequestTargetsVideo()
            self.video = temp_model.from_map(m['Video'])
        return self


class CreateMediaConvertTaskRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
        sources: List[CreateMediaConvertTaskRequestSources] = None,
        tags: Dict[str, Any] = None,
        targets: List[CreateMediaConvertTaskRequestTargets] = None,
        user_data: str = None,
    ):
        self.credential_config = credential_config
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.project_name = project_name
        self.sources = sources
        self.tags = tags
        self.targets = targets
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.sources:
            for k in self.sources:
                if k:
                    k.validate()
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        result['Sources'] = []
        if self.sources is not None:
            for k in self.sources:
                result['Sources'].append(k.to_map() if k else None)
        if self.tags is not None:
            result['Tags'] = self.tags
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        self.sources = []
        if m.get('Sources') is not None:
            for k in m.get('Sources'):
                temp_model = CreateMediaConvertTaskRequestSources()
                self.sources.append(temp_model.from_map(k))
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = CreateMediaConvertTaskRequestTargets()
                self.targets.append(temp_model.from_map(k))
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateMediaConvertTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
        sources_shrink: str = None,
        tags_shrink: str = None,
        targets_shrink: str = None,
        user_data: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.project_name = project_name
        self.sources_shrink = sources_shrink
        self.tags_shrink = tags_shrink
        self.targets_shrink = targets_shrink
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.targets_shrink is not None:
            result['Targets'] = self.targets_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets_shrink = m.get('Targets')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateMediaConvertTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        # 请求 ID
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateMediaConvertTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMediaConvertTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateMediaConvertTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOfficeConversionTaskRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        end_page: int = None,
        first_page: bool = None,
        fit_to_height: bool = None,
        fit_to_width: bool = None,
        hold_line_feed: bool = None,
        image_dpi: int = None,
        long_picture: bool = None,
        long_text: bool = None,
        max_sheet_column: int = None,
        max_sheet_row: int = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        pages: str = None,
        paper_horizontal: bool = None,
        paper_size: str = None,
        password: str = None,
        project_name: str = None,
        quality: int = None,
        scale_percentage: int = None,
        sheet_count: int = None,
        sheet_index: int = None,
        show_comments: bool = None,
        source_type: str = None,
        source_uri: str = None,
        start_page: int = None,
        tags: Dict[str, Any] = None,
        target_type: str = None,
        target_uri: str = None,
        target_uriprefix: str = None,
        trim_policy: TrimPolicy = None,
        user_data: str = None,
    ):
        self.credential_config = credential_config
        # 转换终止页，包含终止页，默认转换到最后一页，表格转图片时需要指定 SheetIndex 才有效
        self.end_page = end_page
        # 表格转图片参数，是否只返回表格的第一张图片，默认为否
        self.first_page = first_page
        # 表格转图片参数，是否将所有行输出到一张图片，默认为否
        self.fit_to_height = fit_to_height
        # 表格转图片参数，是否将所有列输出到一张图片，默认为否
        self.fit_to_width = fit_to_width
        # 转文本时是否保留文档中的换行符，默认不保留
        self.hold_line_feed = hold_line_feed
        # 输出图片 DPI，允许范围 96-600，默认 96
        self.image_dpi = image_dpi
        # 转图片时是否转换成一张长图，最多支持将 20 页合成一张长图，超过可能报错，默认为不转成长图
        self.long_picture = long_picture
        # 转文本时是否转换成长文本，默认每页是个独立的文本
        self.long_text = long_text
        # 表格转图片的最大列数，在 LongPicture 为 true 时生效，默认转所有列
        self.max_sheet_column = max_sheet_column
        # 表格转图片的最大行数，在 LongPicture 为 true 时生效，默认转所有行
        self.max_sheet_row = max_sheet_row
        # mns 消息通知地址
        self.notify_endpoint = notify_endpoint
        # mns 消息通知 topic
        self.notify_topic_name = notify_topic_name
        # 指定转换页码，优先级高于 StartPage/EndPage，格式：多个页码用 “," 拼接，连续页码用 "-" 连接，样例参考: 1,2-4,7
        self.pages = pages
        # 表格转图片纸张是否水平放置，默认为否
        self.paper_horizontal = paper_horizontal
        # 表格转图片纸张大小，支持 A4/A2/A0，默认A4，配合 FitToHeight 或 FitToWidth 一起使用才有效
        self.paper_size = paper_size
        # 文档密码
        self.password = password
        # 项目名称
        self.project_name = project_name
        # 质量参数，范围是0-100，越大质量越好，默认系统自动选择适合的分辨率
        self.quality = quality
        # 缩放参数，允许范围 20~200，100代表不缩放，小于100表示缩小，大于100表示放大，默认不缩放
        self.scale_percentage = scale_percentage
        # 表格转图片参数，指定转换表格中的 sheet 数量，默认转换所有 sheet
        self.sheet_count = sheet_count
        # 表格转图片参数，指定转换哪一个 sheet，从 1 开始，默认从起始页开始转
        self.sheet_index = sheet_index
        # 文字转图片，是否显示批注，目前只支持文字转图片时携带批注，默认不显示批注
        self.show_comments = show_comments
        # 输入文件格式，默认使用文件名后缀小写格式
        self.source_type = source_type
        # 文档转换输入文件地址
        self.source_uri = source_uri
        # 转换起始页，从 1 开始，包含起始页，默认从第一页开始转换，表格转图片时需要指定 SheetIndex 才有效
        self.start_page = start_page
        # 用户自定义标签
        self.tags = tags
        # 输出文件格式
        self.target_type = target_type
        # 文档转换输出地址模式
        self.target_uri = target_uri
        # 文档转换输出文件地址前缀
        self.target_uriprefix = target_uriprefix
        # 表格瘦身
        self.trim_policy = trim_policy
        # 用户自定义数据，在消息通知中返回
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.trim_policy:
            self.trim_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.end_page is not None:
            result['EndPage'] = self.end_page
        if self.first_page is not None:
            result['FirstPage'] = self.first_page
        if self.fit_to_height is not None:
            result['FitToHeight'] = self.fit_to_height
        if self.fit_to_width is not None:
            result['FitToWidth'] = self.fit_to_width
        if self.hold_line_feed is not None:
            result['HoldLineFeed'] = self.hold_line_feed
        if self.image_dpi is not None:
            result['ImageDPI'] = self.image_dpi
        if self.long_picture is not None:
            result['LongPicture'] = self.long_picture
        if self.long_text is not None:
            result['LongText'] = self.long_text
        if self.max_sheet_column is not None:
            result['MaxSheetColumn'] = self.max_sheet_column
        if self.max_sheet_row is not None:
            result['MaxSheetRow'] = self.max_sheet_row
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.paper_horizontal is not None:
            result['PaperHorizontal'] = self.paper_horizontal
        if self.paper_size is not None:
            result['PaperSize'] = self.paper_size
        if self.password is not None:
            result['Password'] = self.password
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.scale_percentage is not None:
            result['ScalePercentage'] = self.scale_percentage
        if self.sheet_count is not None:
            result['SheetCount'] = self.sheet_count
        if self.sheet_index is not None:
            result['SheetIndex'] = self.sheet_index
        if self.show_comments is not None:
            result['ShowComments'] = self.show_comments
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.start_page is not None:
            result['StartPage'] = self.start_page
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.target_uriprefix is not None:
            result['TargetURIPrefix'] = self.target_uriprefix
        if self.trim_policy is not None:
            result['TrimPolicy'] = self.trim_policy.to_map()
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('EndPage') is not None:
            self.end_page = m.get('EndPage')
        if m.get('FirstPage') is not None:
            self.first_page = m.get('FirstPage')
        if m.get('FitToHeight') is not None:
            self.fit_to_height = m.get('FitToHeight')
        if m.get('FitToWidth') is not None:
            self.fit_to_width = m.get('FitToWidth')
        if m.get('HoldLineFeed') is not None:
            self.hold_line_feed = m.get('HoldLineFeed')
        if m.get('ImageDPI') is not None:
            self.image_dpi = m.get('ImageDPI')
        if m.get('LongPicture') is not None:
            self.long_picture = m.get('LongPicture')
        if m.get('LongText') is not None:
            self.long_text = m.get('LongText')
        if m.get('MaxSheetColumn') is not None:
            self.max_sheet_column = m.get('MaxSheetColumn')
        if m.get('MaxSheetRow') is not None:
            self.max_sheet_row = m.get('MaxSheetRow')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('PaperHorizontal') is not None:
            self.paper_horizontal = m.get('PaperHorizontal')
        if m.get('PaperSize') is not None:
            self.paper_size = m.get('PaperSize')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('ScalePercentage') is not None:
            self.scale_percentage = m.get('ScalePercentage')
        if m.get('SheetCount') is not None:
            self.sheet_count = m.get('SheetCount')
        if m.get('SheetIndex') is not None:
            self.sheet_index = m.get('SheetIndex')
        if m.get('ShowComments') is not None:
            self.show_comments = m.get('ShowComments')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('StartPage') is not None:
            self.start_page = m.get('StartPage')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('TargetURIPrefix') is not None:
            self.target_uriprefix = m.get('TargetURIPrefix')
        if m.get('TrimPolicy') is not None:
            temp_model = TrimPolicy()
            self.trim_policy = temp_model.from_map(m['TrimPolicy'])
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateOfficeConversionTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        end_page: int = None,
        first_page: bool = None,
        fit_to_height: bool = None,
        fit_to_width: bool = None,
        hold_line_feed: bool = None,
        image_dpi: int = None,
        long_picture: bool = None,
        long_text: bool = None,
        max_sheet_column: int = None,
        max_sheet_row: int = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        pages: str = None,
        paper_horizontal: bool = None,
        paper_size: str = None,
        password: str = None,
        project_name: str = None,
        quality: int = None,
        scale_percentage: int = None,
        sheet_count: int = None,
        sheet_index: int = None,
        show_comments: bool = None,
        source_type: str = None,
        source_uri: str = None,
        start_page: int = None,
        tags_shrink: str = None,
        target_type: str = None,
        target_uri: str = None,
        target_uriprefix: str = None,
        trim_policy_shrink: str = None,
        user_data: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        # 转换终止页，包含终止页，默认转换到最后一页，表格转图片时需要指定 SheetIndex 才有效
        self.end_page = end_page
        # 表格转图片参数，是否只返回表格的第一张图片，默认为否
        self.first_page = first_page
        # 表格转图片参数，是否将所有行输出到一张图片，默认为否
        self.fit_to_height = fit_to_height
        # 表格转图片参数，是否将所有列输出到一张图片，默认为否
        self.fit_to_width = fit_to_width
        # 转文本时是否保留文档中的换行符，默认不保留
        self.hold_line_feed = hold_line_feed
        # 输出图片 DPI，允许范围 96-600，默认 96
        self.image_dpi = image_dpi
        # 转图片时是否转换成一张长图，最多支持将 20 页合成一张长图，超过可能报错，默认为不转成长图
        self.long_picture = long_picture
        # 转文本时是否转换成长文本，默认每页是个独立的文本
        self.long_text = long_text
        # 表格转图片的最大列数，在 LongPicture 为 true 时生效，默认转所有列
        self.max_sheet_column = max_sheet_column
        # 表格转图片的最大行数，在 LongPicture 为 true 时生效，默认转所有行
        self.max_sheet_row = max_sheet_row
        # mns 消息通知地址
        self.notify_endpoint = notify_endpoint
        # mns 消息通知 topic
        self.notify_topic_name = notify_topic_name
        # 指定转换页码，优先级高于 StartPage/EndPage，格式：多个页码用 “," 拼接，连续页码用 "-" 连接，样例参考: 1,2-4,7
        self.pages = pages
        # 表格转图片纸张是否水平放置，默认为否
        self.paper_horizontal = paper_horizontal
        # 表格转图片纸张大小，支持 A4/A2/A0，默认A4，配合 FitToHeight 或 FitToWidth 一起使用才有效
        self.paper_size = paper_size
        # 文档密码
        self.password = password
        # 项目名称
        self.project_name = project_name
        # 质量参数，范围是0-100，越大质量越好，默认系统自动选择适合的分辨率
        self.quality = quality
        # 缩放参数，允许范围 20~200，100代表不缩放，小于100表示缩小，大于100表示放大，默认不缩放
        self.scale_percentage = scale_percentage
        # 表格转图片参数，指定转换表格中的 sheet 数量，默认转换所有 sheet
        self.sheet_count = sheet_count
        # 表格转图片参数，指定转换哪一个 sheet，从 1 开始，默认从起始页开始转
        self.sheet_index = sheet_index
        # 文字转图片，是否显示批注，目前只支持文字转图片时携带批注，默认不显示批注
        self.show_comments = show_comments
        # 输入文件格式，默认使用文件名后缀小写格式
        self.source_type = source_type
        # 文档转换输入文件地址
        self.source_uri = source_uri
        # 转换起始页，从 1 开始，包含起始页，默认从第一页开始转换，表格转图片时需要指定 SheetIndex 才有效
        self.start_page = start_page
        # 用户自定义标签
        self.tags_shrink = tags_shrink
        # 输出文件格式
        self.target_type = target_type
        # 文档转换输出地址模式
        self.target_uri = target_uri
        # 文档转换输出文件地址前缀
        self.target_uriprefix = target_uriprefix
        # 表格瘦身
        self.trim_policy_shrink = trim_policy_shrink
        # 用户自定义数据，在消息通知中返回
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.end_page is not None:
            result['EndPage'] = self.end_page
        if self.first_page is not None:
            result['FirstPage'] = self.first_page
        if self.fit_to_height is not None:
            result['FitToHeight'] = self.fit_to_height
        if self.fit_to_width is not None:
            result['FitToWidth'] = self.fit_to_width
        if self.hold_line_feed is not None:
            result['HoldLineFeed'] = self.hold_line_feed
        if self.image_dpi is not None:
            result['ImageDPI'] = self.image_dpi
        if self.long_picture is not None:
            result['LongPicture'] = self.long_picture
        if self.long_text is not None:
            result['LongText'] = self.long_text
        if self.max_sheet_column is not None:
            result['MaxSheetColumn'] = self.max_sheet_column
        if self.max_sheet_row is not None:
            result['MaxSheetRow'] = self.max_sheet_row
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.paper_horizontal is not None:
            result['PaperHorizontal'] = self.paper_horizontal
        if self.paper_size is not None:
            result['PaperSize'] = self.paper_size
        if self.password is not None:
            result['Password'] = self.password
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.scale_percentage is not None:
            result['ScalePercentage'] = self.scale_percentage
        if self.sheet_count is not None:
            result['SheetCount'] = self.sheet_count
        if self.sheet_index is not None:
            result['SheetIndex'] = self.sheet_index
        if self.show_comments is not None:
            result['ShowComments'] = self.show_comments
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.start_page is not None:
            result['StartPage'] = self.start_page
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.target_uriprefix is not None:
            result['TargetURIPrefix'] = self.target_uriprefix
        if self.trim_policy_shrink is not None:
            result['TrimPolicy'] = self.trim_policy_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('EndPage') is not None:
            self.end_page = m.get('EndPage')
        if m.get('FirstPage') is not None:
            self.first_page = m.get('FirstPage')
        if m.get('FitToHeight') is not None:
            self.fit_to_height = m.get('FitToHeight')
        if m.get('FitToWidth') is not None:
            self.fit_to_width = m.get('FitToWidth')
        if m.get('HoldLineFeed') is not None:
            self.hold_line_feed = m.get('HoldLineFeed')
        if m.get('ImageDPI') is not None:
            self.image_dpi = m.get('ImageDPI')
        if m.get('LongPicture') is not None:
            self.long_picture = m.get('LongPicture')
        if m.get('LongText') is not None:
            self.long_text = m.get('LongText')
        if m.get('MaxSheetColumn') is not None:
            self.max_sheet_column = m.get('MaxSheetColumn')
        if m.get('MaxSheetRow') is not None:
            self.max_sheet_row = m.get('MaxSheetRow')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('PaperHorizontal') is not None:
            self.paper_horizontal = m.get('PaperHorizontal')
        if m.get('PaperSize') is not None:
            self.paper_size = m.get('PaperSize')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('ScalePercentage') is not None:
            self.scale_percentage = m.get('ScalePercentage')
        if m.get('SheetCount') is not None:
            self.sheet_count = m.get('SheetCount')
        if m.get('SheetIndex') is not None:
            self.sheet_index = m.get('SheetIndex')
        if m.get('ShowComments') is not None:
            self.show_comments = m.get('ShowComments')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('StartPage') is not None:
            self.start_page = m.get('StartPage')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('TargetURIPrefix') is not None:
            self.target_uriprefix = m.get('TargetURIPrefix')
        if m.get('TrimPolicy') is not None:
            self.trim_policy_shrink = m.get('TrimPolicy')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateOfficeConversionTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        # 请求 id
        self.request_id = request_id
        # 任务 id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateOfficeConversionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOfficeConversionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateOfficeConversionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        dataset_max_bind_count: int = None,
        dataset_max_entity_count: int = None,
        dataset_max_file_count: int = None,
        dataset_max_relation_count: int = None,
        dataset_max_total_file_size: int = None,
        description: str = None,
        engine_concurrency: int = None,
        project_max_dataset_count: int = None,
        project_name: str = None,
        project_queries_per_second: int = None,
        service_role: str = None,
        template_id: str = None,
    ):
        self.dataset_max_bind_count = dataset_max_bind_count
        self.dataset_max_entity_count = dataset_max_entity_count
        self.dataset_max_file_count = dataset_max_file_count
        self.dataset_max_relation_count = dataset_max_relation_count
        self.dataset_max_total_file_size = dataset_max_total_file_size
        self.description = description
        self.engine_concurrency = engine_concurrency
        self.project_max_dataset_count = project_max_dataset_count
        # 项目名称
        self.project_name = project_name
        self.project_queries_per_second = project_queries_per_second
        self.service_role = service_role
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.description is not None:
            result['Description'] = self.description
        if self.engine_concurrency is not None:
            result['EngineConcurrency'] = self.engine_concurrency
        if self.project_max_dataset_count is not None:
            result['ProjectMaxDatasetCount'] = self.project_max_dataset_count
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_queries_per_second is not None:
            result['ProjectQueriesPerSecond'] = self.project_queries_per_second
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EngineConcurrency') is not None:
            self.engine_concurrency = m.get('EngineConcurrency')
        if m.get('ProjectMaxDatasetCount') is not None:
            self.project_max_dataset_count = m.get('ProjectMaxDatasetCount')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectQueriesPerSecond') is not None:
            self.project_queries_per_second = m.get('ProjectQueriesPerSecond')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        project: Project = None,
        request_id: str = None,
    ):
        self.project = project
        # 本次请求的唯一 ID
        self.request_id = request_id

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            temp_model = Project()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStoryRequest(TeaModel):
    def __init__(
        self,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        dataset_name: str = None,
        max_file_count: int = None,
        min_file_count: int = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        object_id: str = None,
        project_name: str = None,
        story_end_time: str = None,
        story_name: str = None,
        story_start_time: str = None,
        story_sub_type: str = None,
        story_type: str = None,
        tags: Dict[str, Any] = None,
        user_data: str = None,
    ):
        self.custom_id = custom_id
        self.custom_labels = custom_labels
        self.dataset_name = dataset_name
        self.max_file_count = max_file_count
        self.min_file_count = min_file_count
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.object_id = object_id
        self.project_name = project_name
        self.story_end_time = story_end_time
        self.story_name = story_name
        self.story_start_time = story_start_time
        self.story_sub_type = story_sub_type
        self.story_type = story_type
        self.tags = tags
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_file_count is not None:
            result['MaxFileCount'] = self.max_file_count
        if self.min_file_count is not None:
            result['MinFileCount'] = self.min_file_count
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_end_time is not None:
            result['StoryEndTime'] = self.story_end_time
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_start_time is not None:
            result['StoryStartTime'] = self.story_start_time
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxFileCount') is not None:
            self.max_file_count = m.get('MaxFileCount')
        if m.get('MinFileCount') is not None:
            self.min_file_count = m.get('MinFileCount')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryEndTime') is not None:
            self.story_end_time = m.get('StoryEndTime')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StoryStartTime') is not None:
            self.story_start_time = m.get('StoryStartTime')
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateStoryShrinkRequest(TeaModel):
    def __init__(
        self,
        custom_id: str = None,
        custom_labels_shrink: str = None,
        dataset_name: str = None,
        max_file_count: int = None,
        min_file_count: int = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        object_id: str = None,
        project_name: str = None,
        story_end_time: str = None,
        story_name: str = None,
        story_start_time: str = None,
        story_sub_type: str = None,
        story_type: str = None,
        tags_shrink: str = None,
        user_data: str = None,
    ):
        self.custom_id = custom_id
        self.custom_labels_shrink = custom_labels_shrink
        self.dataset_name = dataset_name
        self.max_file_count = max_file_count
        self.min_file_count = min_file_count
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.object_id = object_id
        self.project_name = project_name
        self.story_end_time = story_end_time
        self.story_name = story_name
        self.story_start_time = story_start_time
        self.story_sub_type = story_sub_type
        self.story_type = story_type
        self.tags_shrink = tags_shrink
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels_shrink is not None:
            result['CustomLabels'] = self.custom_labels_shrink
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_file_count is not None:
            result['MaxFileCount'] = self.max_file_count
        if self.min_file_count is not None:
            result['MinFileCount'] = self.min_file_count
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_end_time is not None:
            result['StoryEndTime'] = self.story_end_time
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_start_time is not None:
            result['StoryStartTime'] = self.story_start_time
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels_shrink = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxFileCount') is not None:
            self.max_file_count = m.get('MaxFileCount')
        if m.get('MinFileCount') is not None:
            self.min_file_count = m.get('MinFileCount')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryEndTime') is not None:
            self.story_end_time = m.get('StoryEndTime')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StoryStartTime') is not None:
            self.story_start_time = m.get('StoryStartTime')
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateStoryResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        # Id of the request
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateStoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateStoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVideoModerationTaskRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        interval: int = None,
        max_frames: int = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
        reviewer: str = None,
        scenes: List[str] = None,
        source_uri: str = None,
        tags: Dict[str, Any] = None,
        user_data: str = None,
    ):
        self.credential_config = credential_config
        self.interval = interval
        self.max_frames = max_frames
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        # 项目名称
        self.project_name = project_name
        self.reviewer = reviewer
        self.scenes = scenes
        self.source_uri = source_uri
        self.tags = tags
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.max_frames is not None:
            result['MaxFrames'] = self.max_frames
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.reviewer is not None:
            result['Reviewer'] = self.reviewer
        if self.scenes is not None:
            result['Scenes'] = self.scenes
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('MaxFrames') is not None:
            self.max_frames = m.get('MaxFrames')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Reviewer') is not None:
            self.reviewer = m.get('Reviewer')
        if m.get('Scenes') is not None:
            self.scenes = m.get('Scenes')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateVideoModerationTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        interval: int = None,
        max_frames: int = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
        reviewer: str = None,
        scenes_shrink: str = None,
        source_uri: str = None,
        tags_shrink: str = None,
        user_data: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        self.interval = interval
        self.max_frames = max_frames
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        # 项目名称
        self.project_name = project_name
        self.reviewer = reviewer
        self.scenes_shrink = scenes_shrink
        self.source_uri = source_uri
        self.tags_shrink = tags_shrink
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.max_frames is not None:
            result['MaxFrames'] = self.max_frames
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.reviewer is not None:
            result['Reviewer'] = self.reviewer
        if self.scenes_shrink is not None:
            result['Scenes'] = self.scenes_shrink
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('MaxFrames') is not None:
            self.max_frames = m.get('MaxFrames')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Reviewer') is not None:
            self.reviewer = m.get('Reviewer')
        if m.get('Scenes') is not None:
            self.scenes_shrink = m.get('Scenes')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateVideoModerationTaskResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.event_id = event_id
        # RequestId
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateVideoModerationTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVideoModerationTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateVideoModerationTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBindingRequest(TeaModel):
    def __init__(
        self,
        cleanup: bool = None,
        dataset_name: str = None,
        project_name: str = None,
        uri: str = None,
    ):
        self.cleanup = cleanup
        self.dataset_name = dataset_name
        # A short description of struct
        self.project_name = project_name
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cleanup is not None:
            result['Cleanup'] = self.cleanup
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cleanup') is not None:
            self.cleanup = m.get('Cleanup')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class DeleteBindingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBindingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBindingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatasetRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DeleteDatasetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDatasetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uri: str = None,
    ):
        self.dataset_name = dataset_name
        self.project_name = project_name
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class DeleteFileMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
    ):
        # 项目名称
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 本次请求的唯一 ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStoryRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        object_id: str = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.object_id = object_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DeleteStoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteStoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteStoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachOSSBucketRequest(TeaModel):
    def __init__(
        self,
        ossbucket: str = None,
    ):
        self.ossbucket = ossbucket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')
        return self


class DetachOSSBucketResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # RequestId
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachOSSBucketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachOSSBucketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DetachOSSBucketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageBodiesRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        sensitivity: float = None,
        source_uri: str = None,
    ):
        self.credential_config = credential_config
        # 项目名称
        self.project_name = project_name
        self.sensitivity = sensitivity
        # SourceURI
        self.source_uri = source_uri

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sensitivity is not None:
            result['Sensitivity'] = self.sensitivity
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sensitivity') is not None:
            self.sensitivity = m.get('Sensitivity')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageBodiesShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        sensitivity: float = None,
        source_uri: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        # 项目名称
        self.project_name = project_name
        self.sensitivity = sensitivity
        # SourceURI
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sensitivity is not None:
            result['Sensitivity'] = self.sensitivity
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sensitivity') is not None:
            self.sensitivity = m.get('Sensitivity')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageBodiesResponseBody(TeaModel):
    def __init__(
        self,
        bodies: List[Body] = None,
        request_id: str = None,
    ):
        # 图片裁剪结果
        self.bodies = bodies
        # 请求唯一ID
        self.request_id = request_id

    def validate(self):
        if self.bodies:
            for k in self.bodies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bodies'] = []
        if self.bodies is not None:
            for k in self.bodies:
                result['Bodies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bodies = []
        if m.get('Bodies') is not None:
            for k in m.get('Bodies'):
                temp_model = Body()
                self.bodies.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageBodiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectImageBodiesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DetectImageBodiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageCodesRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config = credential_config
        # 项目名称
        self.project_name = project_name
        # SourceURI
        self.source_uri = source_uri

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageCodesShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        # 项目名称
        self.project_name = project_name
        # SourceURI
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageCodesResponseBody(TeaModel):
    def __init__(
        self,
        codes: List[Codes] = None,
        request_id: str = None,
    ):
        # 二维码检测结果
        self.codes = codes
        # 请求唯一ID
        self.request_id = request_id

    def validate(self):
        if self.codes:
            for k in self.codes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Codes'] = []
        if self.codes is not None:
            for k in self.codes:
                result['Codes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.codes = []
        if m.get('Codes') is not None:
            for k in m.get('Codes'):
                temp_model = Codes()
                self.codes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageCodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectImageCodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DetectImageCodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageCroppingRequest(TeaModel):
    def __init__(
        self,
        aspect_ratios: str = None,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.aspect_ratios = aspect_ratios
        self.credential_config = credential_config
        # 项目名称
        self.project_name = project_name
        # SourceURI
        self.source_uri = source_uri

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aspect_ratios is not None:
            result['AspectRatios'] = self.aspect_ratios
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AspectRatios') is not None:
            self.aspect_ratios = m.get('AspectRatios')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageCroppingShrinkRequest(TeaModel):
    def __init__(
        self,
        aspect_ratios: str = None,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.aspect_ratios = aspect_ratios
        self.credential_config_shrink = credential_config_shrink
        # 项目名称
        self.project_name = project_name
        # SourceURI
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aspect_ratios is not None:
            result['AspectRatios'] = self.aspect_ratios
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AspectRatios') is not None:
            self.aspect_ratios = m.get('AspectRatios')
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageCroppingResponseBody(TeaModel):
    def __init__(
        self,
        croppings: List[CroppingSuggestion] = None,
        request_id: str = None,
    ):
        # 图片裁剪结果
        self.croppings = croppings
        # 请求唯一ID
        self.request_id = request_id

    def validate(self):
        if self.croppings:
            for k in self.croppings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Croppings'] = []
        if self.croppings is not None:
            for k in self.croppings:
                result['Croppings'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.croppings = []
        if m.get('Croppings') is not None:
            for k in m.get('Croppings'):
                temp_model = CroppingSuggestion()
                self.croppings.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageCroppingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectImageCroppingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DetectImageCroppingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageFacesRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config = credential_config
        # 项目名称
        self.project_name = project_name
        self.source_uri = source_uri

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageFacesShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        # 项目名称
        self.project_name = project_name
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageFacesResponseBody(TeaModel):
    def __init__(
        self,
        faces: List[Figure] = None,
        request_id: str = None,
    ):
        self.faces = faces
        # RequestId
        self.request_id = request_id

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = Figure()
                self.faces.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageFacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectImageFacesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DetectImageFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageLabelsRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        source_uri: str = None,
        threshold: float = None,
    ):
        self.credential_config = credential_config
        # 项目名称
        self.project_name = project_name
        # SourceURI
        self.source_uri = source_uri
        # Threshold
        self.threshold = threshold

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class DetectImageLabelsShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_uri: str = None,
        threshold: float = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        # 项目名称
        self.project_name = project_name
        # SourceURI
        self.source_uri = source_uri
        # Threshold
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class DetectImageLabelsResponseBody(TeaModel):
    def __init__(
        self,
        labels: List[Label] = None,
        request_id: str = None,
    ):
        # 内容标签列表
        self.labels = labels
        # 请求唯一ID
        self.request_id = request_id

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectImageLabelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DetectImageLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageScoreRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config = credential_config
        # 项目名称
        self.project_name = project_name
        self.source_uri = source_uri

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageScoreShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        # 项目名称
        self.project_name = project_name
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageScoreResponseBodyImageScore(TeaModel):
    def __init__(
        self,
        overall_quality_score: float = None,
    ):
        self.overall_quality_score = overall_quality_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overall_quality_score is not None:
            result['OverallQualityScore'] = self.overall_quality_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverallQualityScore') is not None:
            self.overall_quality_score = m.get('OverallQualityScore')
        return self


class DetectImageScoreResponseBody(TeaModel):
    def __init__(
        self,
        image_score: DetectImageScoreResponseBodyImageScore = None,
        request_id: str = None,
    ):
        self.image_score = image_score
        # RequestId
        self.request_id = request_id

    def validate(self):
        if self.image_score:
            self.image_score.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_score is not None:
            result['ImageScore'] = self.image_score.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageScore') is not None:
            temp_model = DetectImageScoreResponseBodyImageScore()
            self.image_score = temp_model.from_map(m['ImageScore'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageScoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectImageScoreResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DetectImageScoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectTextAnomalyRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        project_name: str = None,
    ):
        self.content = content
        # 项目名称
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DetectTextAnomalyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        suggestion: str = None,
    ):
        # RequestId
        self.request_id = request_id
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class DetectTextAnomalyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectTextAnomalyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DetectTextAnomalyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FuzzyQueryRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        project_name: str = None,
        query: str = None,
    ):
        # Dataset 名称
        self.dataset_name = dataset_name
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token
        # 项目名称
        self.project_name = project_name
        # 用于搜索的字符串
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class FuzzyQueryResponseBody(TeaModel):
    def __init__(
        self,
        files: List[File] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.files = files
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # 本次请求的唯一 Id
        self.request_id = request_id

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FuzzyQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FuzzyQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = FuzzyQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBindingRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uri: str = None,
    ):
        self.dataset_name = dataset_name
        self.project_name = project_name
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GetBindingResponseBody(TeaModel):
    def __init__(
        self,
        binding: Binding = None,
        request_id: str = None,
    ):
        self.binding = binding
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.binding:
            self.binding.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binding is not None:
            result['Binding'] = self.binding.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Binding') is not None:
            temp_model = Binding()
            self.binding = temp_model.from_map(m['Binding'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBindingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBindingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatasetRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        with_statistics: bool = None,
    ):
        self.dataset_name = dataset_name
        self.project_name = project_name
        self.with_statistics = with_statistics

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.with_statistics is not None:
            result['WithStatistics'] = self.with_statistics
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('WithStatistics') is not None:
            self.with_statistics = m.get('WithStatistics')
        return self


class GetDatasetResponseBody(TeaModel):
    def __init__(
        self,
        dataset: Dataset = None,
        request_id: str = None,
    ):
        self.dataset = dataset
        self.request_id = request_id

    def validate(self):
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dataset') is not None:
            temp_model = Dataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDatasetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDetectVideoLabelsResultRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # 项目名称
        self.project_name = project_name
        # TaskId
        self.task_id = task_id
        # TaskType
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetDetectVideoLabelsResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        end_time: str = None,
        event_id: str = None,
        labels: List[Label] = None,
        message: str = None,
        project_name: str = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        user_data: str = None,
    ):
        # 任务错误码
        self.code = code
        # 任务结束时间
        self.end_time = end_time
        # 事件Id
        self.event_id = event_id
        # 标签列表
        self.labels = labels
        # 任务错误消息
        self.message = message
        # 项目名称
        self.project_name = project_name
        # 请求唯一Id
        self.request_id = request_id
        # 任务开始时间
        self.start_time = start_time
        # 任务运行状态
        self.status = status
        # 任务唯一ID
        self.task_id = task_id
        # 任务类型
        self.task_type = task_type
        # 用户自定义信息
        self.user_data = user_data

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_id is not None:
            result['EventId'] = self.event_id
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GetDetectVideoLabelsResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDetectVideoLabelsResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetDetectVideoLabelsResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFigureClusterRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        object_id: str = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.object_id = object_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class GetFigureClusterResponseBody(TeaModel):
    def __init__(
        self,
        figure_cluster: FigureCluster = None,
        request_id: str = None,
    ):
        self.figure_cluster = figure_cluster
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.figure_cluster:
            self.figure_cluster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_cluster is not None:
            result['FigureCluster'] = self.figure_cluster.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureCluster') is not None:
            temp_model = FigureCluster()
            self.figure_cluster = temp_model.from_map(m['FigureCluster'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFigureClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFigureClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetFigureClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uri: str = None,
    ):
        self.dataset_name = dataset_name
        self.project_name = project_name
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GetFileMetaResponseBody(TeaModel):
    def __init__(
        self,
        files: List[File] = None,
        request_id: str = None,
    ):
        # File list.
        self.files = files
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaMetaRequest(TeaModel):
    def __init__(
        self,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config = credential_config
        self.project_name = project_name
        self.source_uri = source_uri

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class GetMediaMetaShrinkRequest(TeaModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        self.credential_config_shrink = credential_config_shrink
        self.project_name = project_name
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class GetMediaMetaResponseBody(TeaModel):
    def __init__(
        self,
        addresses: List[Address] = None,
        album: str = None,
        album_artist: str = None,
        artist: str = None,
        audio_streams: List[AudioStream] = None,
        bitrate: int = None,
        composer: str = None,
        duration: float = None,
        format_long_name: str = None,
        format_name: str = None,
        language: str = None,
        lat_long: str = None,
        performer: str = None,
        produce_time: str = None,
        program_count: int = None,
        request_id: str = None,
        size: int = None,
        start_time: float = None,
        stream_count: int = None,
        subtitles: List[SubtitleStream] = None,
        title: str = None,
        video_height: int = None,
        video_streams: List[VideoStream] = None,
        video_width: int = None,
    ):
        self.addresses = addresses
        self.album = album
        self.album_artist = album_artist
        self.artist = artist
        self.audio_streams = audio_streams
        self.bitrate = bitrate
        self.composer = composer
        self.duration = duration
        self.format_long_name = format_long_name
        self.format_name = format_name
        self.language = language
        self.lat_long = lat_long
        self.performer = performer
        self.produce_time = produce_time
        self.program_count = program_count
        self.request_id = request_id
        self.size = size
        self.start_time = start_time
        self.stream_count = stream_count
        self.subtitles = subtitles
        self.title = title
        self.video_height = video_height
        self.video_streams = video_streams
        self.video_width = video_width

    def validate(self):
        if self.addresses:
            for k in self.addresses:
                if k:
                    k.validate()
        if self.audio_streams:
            for k in self.audio_streams:
                if k:
                    k.validate()
        if self.subtitles:
            for k in self.subtitles:
                if k:
                    k.validate()
        if self.video_streams:
            for k in self.video_streams:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Addresses'] = []
        if self.addresses is not None:
            for k in self.addresses:
                result['Addresses'].append(k.to_map() if k else None)
        if self.album is not None:
            result['Album'] = self.album
        if self.album_artist is not None:
            result['AlbumArtist'] = self.album_artist
        if self.artist is not None:
            result['Artist'] = self.artist
        result['AudioStreams'] = []
        if self.audio_streams is not None:
            for k in self.audio_streams:
                result['AudioStreams'].append(k.to_map() if k else None)
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.composer is not None:
            result['Composer'] = self.composer
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.format_long_name is not None:
            result['FormatLongName'] = self.format_long_name
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.language is not None:
            result['Language'] = self.language
        if self.lat_long is not None:
            result['LatLong'] = self.lat_long
        if self.performer is not None:
            result['Performer'] = self.performer
        if self.produce_time is not None:
            result['ProduceTime'] = self.produce_time
        if self.program_count is not None:
            result['ProgramCount'] = self.program_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_count is not None:
            result['StreamCount'] = self.stream_count
        result['Subtitles'] = []
        if self.subtitles is not None:
            for k in self.subtitles:
                result['Subtitles'].append(k.to_map() if k else None)
        if self.title is not None:
            result['Title'] = self.title
        if self.video_height is not None:
            result['VideoHeight'] = self.video_height
        result['VideoStreams'] = []
        if self.video_streams is not None:
            for k in self.video_streams:
                result['VideoStreams'].append(k.to_map() if k else None)
        if self.video_width is not None:
            result['VideoWidth'] = self.video_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addresses = []
        if m.get('Addresses') is not None:
            for k in m.get('Addresses'):
                temp_model = Address()
                self.addresses.append(temp_model.from_map(k))
        if m.get('Album') is not None:
            self.album = m.get('Album')
        if m.get('AlbumArtist') is not None:
            self.album_artist = m.get('AlbumArtist')
        if m.get('Artist') is not None:
            self.artist = m.get('Artist')
        self.audio_streams = []
        if m.get('AudioStreams') is not None:
            for k in m.get('AudioStreams'):
                temp_model = AudioStream()
                self.audio_streams.append(temp_model.from_map(k))
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Composer') is not None:
            self.composer = m.get('Composer')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FormatLongName') is not None:
            self.format_long_name = m.get('FormatLongName')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LatLong') is not None:
            self.lat_long = m.get('LatLong')
        if m.get('Performer') is not None:
            self.performer = m.get('Performer')
        if m.get('ProduceTime') is not None:
            self.produce_time = m.get('ProduceTime')
        if m.get('ProgramCount') is not None:
            self.program_count = m.get('ProgramCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamCount') is not None:
            self.stream_count = m.get('StreamCount')
        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k in m.get('Subtitles'):
                temp_model = SubtitleStream()
                self.subtitles.append(temp_model.from_map(k))
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoHeight') is not None:
            self.video_height = m.get('VideoHeight')
        self.video_streams = []
        if m.get('VideoStreams') is not None:
            for k in m.get('VideoStreams'):
                temp_model = VideoStream()
                self.video_streams.append(temp_model.from_map(k))
        if m.get('VideoWidth') is not None:
            self.video_width = m.get('VideoWidth')
        return self


class GetMediaMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMediaMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetMediaMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOSSBucketAttachmentRequest(TeaModel):
    def __init__(
        self,
        ossbucket: str = None,
    ):
        self.ossbucket = ossbucket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')
        return self


class GetOSSBucketAttachmentResponseBody(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        request_id: str = None,
    ):
        self.project_name = project_name
        # RequestId
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOSSBucketAttachmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOSSBucketAttachmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetOSSBucketAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        with_statistics: bool = None,
    ):
        # 项目名称
        self.project_name = project_name
        # 是否获取详细信息
        self.with_statistics = with_statistics

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.with_statistics is not None:
            result['WithStatistics'] = self.with_statistics
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('WithStatistics') is not None:
            self.with_statistics = m.get('WithStatistics')
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(
        self,
        project: Project = None,
        request_id: str = None,
    ):
        self.project = project
        # RequestId
        self.request_id = request_id

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            temp_model = Project()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStoryRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        object_id: str = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.object_id = object_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class GetStoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        story: Story = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.story = story

    def validate(self):
        if self.story:
            self.story.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.story is not None:
            result['Story'] = self.story.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Story') is not None:
            temp_model = Story()
            self.story = temp_model.from_map(m['Story'])
        return self


class GetStoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # 项目名称
        self.project_name = project_name
        # TaskId
        self.task_id = task_id
        # TaskType
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        end_time: str = None,
        event_id: str = None,
        message: str = None,
        project_name: str = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        tags: Dict[str, Any] = None,
        task_id: str = None,
        task_type: str = None,
        user_data: str = None,
    ):
        # 任务错误码
        self.code = code
        # 任务结束时间
        self.end_time = end_time
        # 事件Id
        self.event_id = event_id
        # 任务错误消息
        self.message = message
        # 项目名称
        self.project_name = project_name
        # 请求唯一Id
        self.request_id = request_id
        # 任务开始时间
        self.start_time = start_time
        # 任务运行状态
        self.status = status
        self.tags = tags
        # 任务唯一ID
        self.task_id = task_id
        # 任务类型
        self.task_type = task_type
        # 用户自定义信息
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.message is not None:
            result['Message'] = self.message
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GetTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebofficeURLRequest(TeaModel):
    def __init__(
        self,
        cache_preview: bool = None,
        credential_config: CredentialConfig = None,
        external_uploaded: bool = None,
        filename: str = None,
        hidecmb: bool = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        password: str = None,
        permission: WebofficePermission = None,
        preview_pages: int = None,
        project_name: str = None,
        referer: str = None,
        source_uri: str = None,
        user: WebofficeUser = None,
        user_data: str = None,
        watermark: WebofficeWatermark = None,
    ):
        # 缓存预览标识
        self.cache_preview = cache_preview
        self.credential_config = credential_config
        # 是否支持外部上传
        self.external_uploaded = external_uploaded
        # 文件名，必须带文件名后缀，默认是 SourceUri 的最后一级
        self.filename = filename
        # 隐藏工具栏，预览模式下使用
        self.hidecmb = hidecmb
        # mns 消息通知地址
        self.notify_endpoint = notify_endpoint
        # mns 消息通知 topic
        self.notify_topic_name = notify_topic_name
        # 文件密码
        self.password = password
        # 权限
        self.permission = permission
        # 预览前几页
        self.preview_pages = preview_pages
        # 项目名称
        self.project_name = project_name
        # oss 防盗链 referer
        self.referer = referer
        # 预览编辑地址
        self.source_uri = source_uri
        # 用户
        self.user = user
        # 用户自定义数据，在消息通知中返回
        self.user_data = user_data
        # 水印
        self.watermark = watermark

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.permission:
            self.permission.validate()
        if self.user:
            self.user.validate()
        if self.watermark:
            self.watermark.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_preview is not None:
            result['CachePreview'] = self.cache_preview
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.external_uploaded is not None:
            result['ExternalUploaded'] = self.external_uploaded
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.hidecmb is not None:
            result['Hidecmb'] = self.hidecmb
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.password is not None:
            result['Password'] = self.password
        if self.permission is not None:
            result['Permission'] = self.permission.to_map()
        if self.preview_pages is not None:
            result['PreviewPages'] = self.preview_pages
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.referer is not None:
            result['Referer'] = self.referer
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.user is not None:
            result['User'] = self.user.to_map()
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.watermark is not None:
            result['Watermark'] = self.watermark.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CachePreview') is not None:
            self.cache_preview = m.get('CachePreview')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ExternalUploaded') is not None:
            self.external_uploaded = m.get('ExternalUploaded')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('Hidecmb') is not None:
            self.hidecmb = m.get('Hidecmb')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Permission') is not None:
            temp_model = WebofficePermission()
            self.permission = temp_model.from_map(m['Permission'])
        if m.get('PreviewPages') is not None:
            self.preview_pages = m.get('PreviewPages')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Referer') is not None:
            self.referer = m.get('Referer')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('User') is not None:
            temp_model = WebofficeUser()
            self.user = temp_model.from_map(m['User'])
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Watermark') is not None:
            temp_model = WebofficeWatermark()
            self.watermark = temp_model.from_map(m['Watermark'])
        return self


class GetWebofficeURLShrinkRequest(TeaModel):
    def __init__(
        self,
        cache_preview: bool = None,
        credential_config_shrink: str = None,
        external_uploaded: bool = None,
        filename: str = None,
        hidecmb: bool = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        password: str = None,
        permission_shrink: str = None,
        preview_pages: int = None,
        project_name: str = None,
        referer: str = None,
        source_uri: str = None,
        user_shrink: str = None,
        user_data: str = None,
        watermark_shrink: str = None,
    ):
        # 缓存预览标识
        self.cache_preview = cache_preview
        self.credential_config_shrink = credential_config_shrink
        # 是否支持外部上传
        self.external_uploaded = external_uploaded
        # 文件名，必须带文件名后缀，默认是 SourceUri 的最后一级
        self.filename = filename
        # 隐藏工具栏，预览模式下使用
        self.hidecmb = hidecmb
        # mns 消息通知地址
        self.notify_endpoint = notify_endpoint
        # mns 消息通知 topic
        self.notify_topic_name = notify_topic_name
        # 文件密码
        self.password = password
        # 权限
        self.permission_shrink = permission_shrink
        # 预览前几页
        self.preview_pages = preview_pages
        # 项目名称
        self.project_name = project_name
        # oss 防盗链 referer
        self.referer = referer
        # 预览编辑地址
        self.source_uri = source_uri
        # 用户
        self.user_shrink = user_shrink
        # 用户自定义数据，在消息通知中返回
        self.user_data = user_data
        # 水印
        self.watermark_shrink = watermark_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_preview is not None:
            result['CachePreview'] = self.cache_preview
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.external_uploaded is not None:
            result['ExternalUploaded'] = self.external_uploaded
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.hidecmb is not None:
            result['Hidecmb'] = self.hidecmb
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.password is not None:
            result['Password'] = self.password
        if self.permission_shrink is not None:
            result['Permission'] = self.permission_shrink
        if self.preview_pages is not None:
            result['PreviewPages'] = self.preview_pages
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.referer is not None:
            result['Referer'] = self.referer
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.user_shrink is not None:
            result['User'] = self.user_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.watermark_shrink is not None:
            result['Watermark'] = self.watermark_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CachePreview') is not None:
            self.cache_preview = m.get('CachePreview')
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ExternalUploaded') is not None:
            self.external_uploaded = m.get('ExternalUploaded')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('Hidecmb') is not None:
            self.hidecmb = m.get('Hidecmb')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Permission') is not None:
            self.permission_shrink = m.get('Permission')
        if m.get('PreviewPages') is not None:
            self.preview_pages = m.get('PreviewPages')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Referer') is not None:
            self.referer = m.get('Referer')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('User') is not None:
            self.user_shrink = m.get('User')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Watermark') is not None:
            self.watermark_shrink = m.get('Watermark')
        return self


class GetWebofficeURLResponseBody(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        access_token_expired_time: str = None,
        refresh_token: str = None,
        refresh_token_expired_time: str = None,
        request_id: str = None,
        weboffice_url: str = None,
    ):
        # access token
        self.access_token = access_token
        # access token 过期时间
        self.access_token_expired_time = access_token_expired_time
        # refresh token
        self.refresh_token = refresh_token
        # refresh token 过期时间
        self.refresh_token_expired_time = refresh_token_expired_time
        # 请求 id
        self.request_id = request_id
        # 预览编辑地址
        self.weboffice_url = weboffice_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.weboffice_url is not None:
            result['WebofficeURL'] = self.weboffice_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WebofficeURL') is not None:
            self.weboffice_url = m.get('WebofficeURL')
        return self


class GetWebofficeURLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWebofficeURLResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetWebofficeURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IndexFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        file: FileForReq = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.file = file
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.project_name = project_name

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.file is not None:
            result['File'] = self.file.to_map()
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('File') is not None:
            temp_model = FileForReq()
            self.file = temp_model.from_map(m['File'])
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class IndexFileMetaShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        file_shrink: str = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.file_shrink = file_shrink
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.file_shrink is not None:
            result['File'] = self.file_shrink
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('File') is not None:
            self.file_shrink = m.get('File')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class IndexFileMetaResponseBody(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        request_id: str = None,
    ):
        self.event_id = event_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IndexFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IndexFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = IndexFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBindingsRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.max_results = max_results
        self.next_token = next_token
        # A short description of struct
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ListBindingsResponseBody(TeaModel):
    def __init__(
        self,
        bindings: List[Binding] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.bindings = bindings
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = Binding()
                self.bindings.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBindingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBindingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasetsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        prefix: str = None,
        project_name: str = None,
    ):
        # 返回最大个数
        self.max_results = max_results
        # 当总结果个数大于MaxResults时，用于翻页的token
        self.next_token = next_token
        self.prefix = prefix
        # 项目名称
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ListDatasetsResponseBody(TeaModel):
    def __init__(
        self,
        datasets: List[Dataset] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # Datasets
        self.datasets = datasets
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = Dataset()
                self.datasets.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDatasetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatasetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListDatasetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        prefix: str = None,
    ):
        # 返回结果的最大个数
        self.max_results = max_results
        # 当总结果个数大于MaxResults时，用于翻页的token
        self.next_token = next_token
        # 列出包含某前缀的project
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        projects: List[Project] = None,
        request_id: str = None,
    ):
        # 当总结果个数大于MaxResults时，用于翻页的token
        self.next_token = next_token
        # 由ProjectItem组成的数组
        self.projects = projects
        # 本次请求的唯一 ID
        self.request_id = request_id

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['Projects'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.projects = []
        if m.get('Projects') is not None:
            for k in m.get('Projects'):
                temp_model = Project()
                self.projects.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[RegionType] = None,
        request_id: str = None,
    ):
        self.regions = regions
        # RequestId
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = RegionType()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(
        self,
        end_time_range: TimeRange = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
        start_time_range: TimeRange = None,
        status: str = None,
        tag_selector: str = None,
        task_types: List[str] = None,
    ):
        self.end_time_range = end_time_range
        # MaxResults
        self.max_results = max_results
        # NextToken
        self.next_token = next_token
        self.order = order
        # 项目名称
        self.project_name = project_name
        self.sort = sort
        self.start_time_range = start_time_range
        self.status = status
        self.tag_selector = tag_selector
        self.task_types = task_types

    def validate(self):
        if self.end_time_range:
            self.end_time_range.validate()
        if self.start_time_range:
            self.start_time_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time_range is not None:
            result['EndTimeRange'] = self.end_time_range.to_map()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_time_range is not None:
            result['StartTimeRange'] = self.start_time_range.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_selector is not None:
            result['TagSelector'] = self.tag_selector
        if self.task_types is not None:
            result['TaskTypes'] = self.task_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimeRange') is not None:
            temp_model = TimeRange()
            self.end_time_range = temp_model.from_map(m['EndTimeRange'])
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartTimeRange') is not None:
            temp_model = TimeRange()
            self.start_time_range = temp_model.from_map(m['StartTimeRange'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagSelector') is not None:
            self.tag_selector = m.get('TagSelector')
        if m.get('TaskTypes') is not None:
            self.task_types = m.get('TaskTypes')
        return self


class ListTasksShrinkRequest(TeaModel):
    def __init__(
        self,
        end_time_range_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
        start_time_range_shrink: str = None,
        status: str = None,
        tag_selector: str = None,
        task_types_shrink: str = None,
    ):
        self.end_time_range_shrink = end_time_range_shrink
        # MaxResults
        self.max_results = max_results
        # NextToken
        self.next_token = next_token
        self.order = order
        # 项目名称
        self.project_name = project_name
        self.sort = sort
        self.start_time_range_shrink = start_time_range_shrink
        self.status = status
        self.tag_selector = tag_selector
        self.task_types_shrink = task_types_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time_range_shrink is not None:
            result['EndTimeRange'] = self.end_time_range_shrink
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_time_range_shrink is not None:
            result['StartTimeRange'] = self.start_time_range_shrink
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_selector is not None:
            result['TagSelector'] = self.tag_selector
        if self.task_types_shrink is not None:
            result['TaskTypes'] = self.task_types_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimeRange') is not None:
            self.end_time_range_shrink = m.get('EndTimeRange')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartTimeRange') is not None:
            self.start_time_range_shrink = m.get('StartTimeRange')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagSelector') is not None:
            self.tag_selector = m.get('TagSelector')
        if m.get('TaskTypes') is not None:
            self.task_types_shrink = m.get('TaskTypes')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        project_name: str = None,
        request_id: str = None,
        tasks: List[TaskInfo] = None,
    ):
        # 最大结果数量
        self.max_results = max_results
        # 翻页标记
        self.next_token = next_token
        # 项目名称
        self.project_name = project_name
        # 请求唯一Id
        self.request_id = request_id
        # 任务信息
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = TaskInfo()
                self.tasks.append(temp_model.from_map(k))
        return self


class ListTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MergeFigureClustersRequest(TeaModel):
    def __init__(
        self,
        cluster_id_from: str = None,
        cluster_id_to: str = None,
        custom_message: str = None,
        dataset_name: str = None,
        figure_type: str = None,
        notify_topic_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
    ):
        self.cluster_id_from = cluster_id_from
        self.cluster_id_to = cluster_id_to
        self.custom_message = custom_message
        self.dataset_name = dataset_name
        self.figure_type = figure_type
        self.notify_topic_endpoint = notify_topic_endpoint
        self.notify_topic_name = notify_topic_name
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id_from is not None:
            result['ClusterIdFrom'] = self.cluster_id_from
        if self.cluster_id_to is not None:
            result['ClusterIdTo'] = self.cluster_id_to
        if self.custom_message is not None:
            result['CustomMessage'] = self.custom_message
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.figure_type is not None:
            result['FigureType'] = self.figure_type
        if self.notify_topic_endpoint is not None:
            result['NotifyTopicEndpoint'] = self.notify_topic_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIdFrom') is not None:
            self.cluster_id_from = m.get('ClusterIdFrom')
        if m.get('ClusterIdTo') is not None:
            self.cluster_id_to = m.get('ClusterIdTo')
        if m.get('CustomMessage') is not None:
            self.custom_message = m.get('CustomMessage')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FigureType') is not None:
            self.figure_type = m.get('FigureType')
        if m.get('NotifyTopicEndpoint') is not None:
            self.notify_topic_endpoint = m.get('NotifyTopicEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class MergeFigureClustersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class MergeFigureClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MergeFigureClustersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = MergeFigureClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFigureClustersRequest(TeaModel):
    def __init__(
        self,
        custom_labels: str = None,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
    ):
        self.custom_labels = custom_labels
        self.dataset_name = dataset_name
        self.max_results = max_results
        self.next_token = next_token
        # 升降序
        self.order = order
        self.project_name = project_name
        # 排序字段
        self.sort = sort

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class QueryFigureClustersResponseBody(TeaModel):
    def __init__(
        self,
        figure_clusters: List[FigureCluster] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.figure_clusters = figure_clusters
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.figure_clusters:
            for k in self.figure_clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FigureClusters'] = []
        if self.figure_clusters is not None:
            for k in self.figure_clusters:
                result['FigureClusters'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.figure_clusters = []
        if m.get('FigureClusters') is not None:
            for k in m.get('FigureClusters'):
                temp_model = FigureCluster()
                self.figure_clusters.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryFigureClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFigureClustersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = QueryFigureClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStoriesRequest(TeaModel):
    def __init__(
        self,
        create_time_range: TimeRange = None,
        custom_labels: str = None,
        dataset_name: str = None,
        figure_cluster_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        object_id: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
        story_end_time_range: TimeRange = None,
        story_name: str = None,
        story_start_time_range: TimeRange = None,
        story_sub_type: str = None,
        story_type: str = None,
        with_empty_stories: bool = None,
    ):
        self.create_time_range = create_time_range
        self.custom_labels = custom_labels
        self.dataset_name = dataset_name
        self.figure_cluster_ids = figure_cluster_ids
        self.max_results = max_results
        self.next_token = next_token
        self.object_id = object_id
        self.order = order
        self.project_name = project_name
        self.sort = sort
        self.story_end_time_range = story_end_time_range
        self.story_name = story_name
        self.story_start_time_range = story_start_time_range
        self.story_sub_type = story_sub_type
        self.story_type = story_type
        self.with_empty_stories = with_empty_stories

    def validate(self):
        if self.create_time_range:
            self.create_time_range.validate()
        if self.story_end_time_range:
            self.story_end_time_range.validate()
        if self.story_start_time_range:
            self.story_start_time_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_range is not None:
            result['CreateTimeRange'] = self.create_time_range.to_map()
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.figure_cluster_ids is not None:
            result['FigureClusterIds'] = self.figure_cluster_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.story_end_time_range is not None:
            result['StoryEndTimeRange'] = self.story_end_time_range.to_map()
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_start_time_range is not None:
            result['StoryStartTimeRange'] = self.story_start_time_range.to_map()
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        if self.with_empty_stories is not None:
            result['WithEmptyStories'] = self.with_empty_stories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeRange') is not None:
            temp_model = TimeRange()
            self.create_time_range = temp_model.from_map(m['CreateTimeRange'])
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FigureClusterIds') is not None:
            self.figure_cluster_ids = m.get('FigureClusterIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StoryEndTimeRange') is not None:
            temp_model = TimeRange()
            self.story_end_time_range = temp_model.from_map(m['StoryEndTimeRange'])
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StoryStartTimeRange') is not None:
            temp_model = TimeRange()
            self.story_start_time_range = temp_model.from_map(m['StoryStartTimeRange'])
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        if m.get('WithEmptyStories') is not None:
            self.with_empty_stories = m.get('WithEmptyStories')
        return self


class QueryStoriesShrinkRequest(TeaModel):
    def __init__(
        self,
        create_time_range_shrink: str = None,
        custom_labels: str = None,
        dataset_name: str = None,
        figure_cluster_ids_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        object_id: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
        story_end_time_range_shrink: str = None,
        story_name: str = None,
        story_start_time_range_shrink: str = None,
        story_sub_type: str = None,
        story_type: str = None,
        with_empty_stories: bool = None,
    ):
        self.create_time_range_shrink = create_time_range_shrink
        self.custom_labels = custom_labels
        self.dataset_name = dataset_name
        self.figure_cluster_ids_shrink = figure_cluster_ids_shrink
        self.max_results = max_results
        self.next_token = next_token
        self.object_id = object_id
        self.order = order
        self.project_name = project_name
        self.sort = sort
        self.story_end_time_range_shrink = story_end_time_range_shrink
        self.story_name = story_name
        self.story_start_time_range_shrink = story_start_time_range_shrink
        self.story_sub_type = story_sub_type
        self.story_type = story_type
        self.with_empty_stories = with_empty_stories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_range_shrink is not None:
            result['CreateTimeRange'] = self.create_time_range_shrink
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.figure_cluster_ids_shrink is not None:
            result['FigureClusterIds'] = self.figure_cluster_ids_shrink
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.story_end_time_range_shrink is not None:
            result['StoryEndTimeRange'] = self.story_end_time_range_shrink
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_start_time_range_shrink is not None:
            result['StoryStartTimeRange'] = self.story_start_time_range_shrink
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        if self.with_empty_stories is not None:
            result['WithEmptyStories'] = self.with_empty_stories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeRange') is not None:
            self.create_time_range_shrink = m.get('CreateTimeRange')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FigureClusterIds') is not None:
            self.figure_cluster_ids_shrink = m.get('FigureClusterIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StoryEndTimeRange') is not None:
            self.story_end_time_range_shrink = m.get('StoryEndTimeRange')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StoryStartTimeRange') is not None:
            self.story_start_time_range_shrink = m.get('StoryStartTimeRange')
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        if m.get('WithEmptyStories') is not None:
            self.with_empty_stories = m.get('WithEmptyStories')
        return self


class QueryStoriesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        stories: List[Story] = None,
    ):
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.stories = stories

    def validate(self):
        if self.stories:
            for k in self.stories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Stories'] = []
        if self.stories is not None:
            for k in self.stories:
                result['Stories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stories = []
        if m.get('Stories') is not None:
            for k in m.get('Stories'):
                temp_model = Story()
                self.stories.append(temp_model.from_map(k))
        return self


class QueryStoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryStoriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = QueryStoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshWebofficeTokenRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        credential_config: CredentialConfig = None,
        project_name: str = None,
        refresh_token: str = None,
    ):
        # access token
        self.access_token = access_token
        self.credential_config = credential_config
        # 项目名称
        self.project_name = project_name
        # refresh token
        self.refresh_token = refresh_token

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        return self


class RefreshWebofficeTokenShrinkRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        credential_config_shrink: str = None,
        project_name: str = None,
        refresh_token: str = None,
    ):
        # access token
        self.access_token = access_token
        self.credential_config_shrink = credential_config_shrink
        # 项目名称
        self.project_name = project_name
        # refresh token
        self.refresh_token = refresh_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        return self


class RefreshWebofficeTokenResponseBody(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        access_token_expired_time: str = None,
        refresh_token: str = None,
        refresh_token_expired_time: str = None,
        request_id: str = None,
    ):
        # access token
        self.access_token = access_token
        # access token 过期时间
        self.access_token_expired_time = access_token_expired_time
        # refresh token
        self.refresh_token = refresh_token
        # refresh token 过期时间
        self.refresh_token_expired_time = refresh_token_expired_time
        # 请求 Id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefreshWebofficeTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshWebofficeTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = RefreshWebofficeTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveStoryFilesRequestFiles(TeaModel):
    def __init__(
        self,
        uri: str = None,
    ):
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class RemoveStoryFilesRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        files: List[RemoveStoryFilesRequestFiles] = None,
        object_id: str = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.files = files
        self.object_id = object_id
        # A short description of struct
        self.project_name = project_name

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = RemoveStoryFilesRequestFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class RemoveStoryFilesShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        files_shrink: str = None,
        object_id: str = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.files_shrink = files_shrink
        self.object_id = object_id
        # A short description of struct
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class RemoveStoryFilesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveStoryFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveStoryFilesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = RemoveStoryFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeBindingRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uri: str = None,
    ):
        self.dataset_name = dataset_name
        self.project_name = project_name
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class ResumeBindingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResumeBindingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResumeBindingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ResumeBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SemanticQueryRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        project_name: str = None,
        query: str = None,
    ):
        # Dataset 名称
        self.dataset_name = dataset_name
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token
        # 项目名称
        self.project_name = project_name
        # 需要搜索的内容，使用自然语言描述
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class SemanticQueryResponseBodyAggregationsGroups(TeaModel):
    def __init__(
        self,
        count: int = None,
        value: str = None,
    ):
        # 分组聚合的计数
        self.count = count
        # 分组聚合的值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SemanticQueryResponseBodyAggregations(TeaModel):
    def __init__(
        self,
        field: str = None,
        groups: List[SemanticQueryResponseBodyAggregationsGroups] = None,
        operation: str = None,
        value: float = None,
    ):
        # 聚合字段名
        self.field = field
        # 分组聚合的结果
        self.groups = groups
        # 聚合字段的聚合操作符
        self.operation = operation
        # 聚合的统计结果
        self.value = value

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = SemanticQueryResponseBodyAggregationsGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SemanticQueryResponseBody(TeaModel):
    def __init__(
        self,
        aggregations: List[SemanticQueryResponseBodyAggregations] = None,
        files: List[File] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # 聚合字段的字段名
        self.aggregations = aggregations
        # 文件列表
        self.files = files
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # 本次请求的唯一 Id
        self.request_id = request_id

    def validate(self):
        if self.aggregations:
            for k in self.aggregations:
                if k:
                    k.validate()
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Aggregations'] = []
        if self.aggregations is not None:
            for k in self.aggregations:
                result['Aggregations'].append(k.to_map() if k else None)
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aggregations = []
        if m.get('Aggregations') is not None:
            for k in m.get('Aggregations'):
                temp_model = SemanticQueryResponseBodyAggregations()
                self.aggregations.append(temp_model.from_map(k))
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SemanticQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SemanticQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SemanticQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SimpleQueryRequestAggregations(TeaModel):
    def __init__(
        self,
        field: str = None,
        operation: str = None,
    ):
        # 聚合字段的字段名
        self.field = field
        # 聚合字段的聚合操作符
        self.operation = operation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.operation is not None:
            result['Operation'] = self.operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        return self


class SimpleQueryRequest(TeaModel):
    def __init__(
        self,
        aggregations: List[SimpleQueryRequestAggregations] = None,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        query: SimpleQuery = None,
        sort: str = None,
        with_fields: List[str] = None,
    ):
        # 聚合字段
        self.aggregations = aggregations
        # Dataset 名称
        self.dataset_name = dataset_name
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token
        # 排序字段
        self.order = order
        # 项目名称
        self.project_name = project_name
        self.query = query
        # 排序方式，默认 DESC
        self.sort = sort
        # 仅返回哪些字段
        self.with_fields = with_fields

    def validate(self):
        if self.aggregations:
            for k in self.aggregations:
                if k:
                    k.validate()
        if self.query:
            self.query.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Aggregations'] = []
        if self.aggregations is not None:
            for k in self.aggregations:
                result['Aggregations'].append(k.to_map() if k else None)
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.query is not None:
            result['Query'] = self.query.to_map()
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.with_fields is not None:
            result['WithFields'] = self.with_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aggregations = []
        if m.get('Aggregations') is not None:
            for k in m.get('Aggregations'):
                temp_model = SimpleQueryRequestAggregations()
                self.aggregations.append(temp_model.from_map(k))
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Query') is not None:
            temp_model = SimpleQuery()
            self.query = temp_model.from_map(m['Query'])
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('WithFields') is not None:
            self.with_fields = m.get('WithFields')
        return self


class SimpleQueryShrinkRequest(TeaModel):
    def __init__(
        self,
        aggregations_shrink: str = None,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        query_shrink: str = None,
        sort: str = None,
        with_fields_shrink: str = None,
    ):
        # 聚合字段
        self.aggregations_shrink = aggregations_shrink
        # Dataset 名称
        self.dataset_name = dataset_name
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token
        # 排序字段
        self.order = order
        # 项目名称
        self.project_name = project_name
        self.query_shrink = query_shrink
        # 排序方式，默认 DESC
        self.sort = sort
        # 仅返回哪些字段
        self.with_fields_shrink = with_fields_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregations_shrink is not None:
            result['Aggregations'] = self.aggregations_shrink
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.query_shrink is not None:
            result['Query'] = self.query_shrink
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.with_fields_shrink is not None:
            result['WithFields'] = self.with_fields_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregations') is not None:
            self.aggregations_shrink = m.get('Aggregations')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Query') is not None:
            self.query_shrink = m.get('Query')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('WithFields') is not None:
            self.with_fields_shrink = m.get('WithFields')
        return self


class SimpleQueryResponseBodyAggregationsGroups(TeaModel):
    def __init__(
        self,
        count: int = None,
        value: str = None,
    ):
        # 分组聚合的计数
        self.count = count
        # 分组聚合的值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SimpleQueryResponseBodyAggregations(TeaModel):
    def __init__(
        self,
        field: str = None,
        groups: List[SimpleQueryResponseBodyAggregationsGroups] = None,
        operation: str = None,
        value: float = None,
    ):
        # 聚合字段名
        self.field = field
        # 分组聚合的结果
        self.groups = groups
        # 聚合字段的聚合操作符
        self.operation = operation
        self.value = value

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = SimpleQueryResponseBodyAggregationsGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SimpleQueryResponseBody(TeaModel):
    def __init__(
        self,
        aggregations: List[SimpleQueryResponseBodyAggregations] = None,
        files: List[File] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # 聚合字段的字段名
        self.aggregations = aggregations
        # 文件列表
        self.files = files
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # 本次请求的唯一 Id
        self.request_id = request_id

    def validate(self):
        if self.aggregations:
            for k in self.aggregations:
                if k:
                    k.validate()
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Aggregations'] = []
        if self.aggregations is not None:
            for k in self.aggregations:
                result['Aggregations'].append(k.to_map() if k else None)
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aggregations = []
        if m.get('Aggregations') is not None:
            for k in m.get('Aggregations'):
                temp_model = SimpleQueryResponseBodyAggregations()
                self.aggregations.append(temp_model.from_map(k))
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SimpleQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SimpleQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SimpleQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopBindingRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        reason: str = None,
        uri: str = None,
    ):
        self.dataset_name = dataset_name
        self.project_name = project_name
        self.reason = reason
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class StopBindingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopBindingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopBindingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = StopBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDatasetRequest(TeaModel):
    def __init__(
        self,
        dataset_max_bind_count: int = None,
        dataset_max_entity_count: int = None,
        dataset_max_file_count: int = None,
        dataset_max_relation_count: int = None,
        dataset_max_total_file_size: int = None,
        dataset_name: str = None,
        description: str = None,
        project_name: str = None,
        template_id: str = None,
    ):
        # 媒体集最多绑定数
        self.dataset_max_bind_count = dataset_max_bind_count
        # 媒体集最多实体数
        self.dataset_max_entity_count = dataset_max_entity_count
        # 媒体集最多文件数
        self.dataset_max_file_count = dataset_max_file_count
        # 媒体集最多关系数
        self.dataset_max_relation_count = dataset_max_relation_count
        # 媒体集最大文件总大小
        self.dataset_max_total_file_size = dataset_max_total_file_size
        # 媒体集名称
        self.dataset_name = dataset_name
        # 描述
        self.description = description
        # 项目名称
        self.project_name = project_name
        # 模板Id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateDatasetResponseBody(TeaModel):
    def __init__(
        self,
        dataset: Dataset = None,
        request_id: str = None,
    ):
        self.dataset = dataset
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dataset') is not None:
            temp_model = Dataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDatasetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFigureClusterRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        figure_cluster: FigureClusterForReq = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.figure_cluster = figure_cluster
        self.project_name = project_name

    def validate(self):
        if self.figure_cluster:
            self.figure_cluster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.figure_cluster is not None:
            result['FigureCluster'] = self.figure_cluster.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FigureCluster') is not None:
            temp_model = FigureClusterForReq()
            self.figure_cluster = temp_model.from_map(m['FigureCluster'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class UpdateFigureClusterShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        figure_cluster_shrink: str = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.figure_cluster_shrink = figure_cluster_shrink
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.figure_cluster_shrink is not None:
            result['FigureCluster'] = self.figure_cluster_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FigureCluster') is not None:
            self.figure_cluster_shrink = m.get('FigureCluster')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class UpdateFigureClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateFigureClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFigureClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateFigureClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        file: FileForReq = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.file = file
        self.project_name = project_name

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.file is not None:
            result['File'] = self.file.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('File') is not None:
            temp_model = FileForReq()
            self.file = temp_model.from_map(m['File'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class UpdateFileMetaShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        file_shrink: str = None,
        project_name: str = None,
    ):
        self.dataset_name = dataset_name
        self.file_shrink = file_shrink
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.file_shrink is not None:
            result['File'] = self.file_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('File') is not None:
            self.file_shrink = m.get('File')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class UpdateFileMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(
        self,
        dataset_max_bind_count: int = None,
        dataset_max_entity_count: int = None,
        dataset_max_file_count: int = None,
        dataset_max_relation_count: int = None,
        dataset_max_total_file_size: int = None,
        description: str = None,
        engine_concurrency: int = None,
        project_max_dataset_count: int = None,
        project_name: str = None,
        project_queries_per_second: int = None,
        service_role: str = None,
        template_id: str = None,
    ):
        # 媒体集最多绑定数
        self.dataset_max_bind_count = dataset_max_bind_count
        # 媒体集最多实体数
        self.dataset_max_entity_count = dataset_max_entity_count
        # 媒体集最多文件数
        self.dataset_max_file_count = dataset_max_file_count
        # 媒体集最多关系数
        self.dataset_max_relation_count = dataset_max_relation_count
        # 媒体集最大文件总大小
        self.dataset_max_total_file_size = dataset_max_total_file_size
        # 项目描述
        self.description = description
        # 项目并发数
        self.engine_concurrency = engine_concurrency
        # 项目最多媒体集数
        self.project_max_dataset_count = project_max_dataset_count
        # 项目名称
        self.project_name = project_name
        # 项目QPS
        self.project_queries_per_second = project_queries_per_second
        # 服务角色
        self.service_role = service_role
        # 模板Id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.description is not None:
            result['Description'] = self.description
        if self.engine_concurrency is not None:
            result['EngineConcurrency'] = self.engine_concurrency
        if self.project_max_dataset_count is not None:
            result['ProjectMaxDatasetCount'] = self.project_max_dataset_count
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_queries_per_second is not None:
            result['ProjectQueriesPerSecond'] = self.project_queries_per_second
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EngineConcurrency') is not None:
            self.engine_concurrency = m.get('EngineConcurrency')
        if m.get('ProjectMaxDatasetCount') is not None:
            self.project_max_dataset_count = m.get('ProjectMaxDatasetCount')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectQueriesPerSecond') is not None:
            self.project_queries_per_second = m.get('ProjectQueriesPerSecond')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateProjectResponseBody(TeaModel):
    def __init__(
        self,
        project: Project = None,
        request_id: str = None,
    ):
        self.project = project
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            temp_model = Project()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStoryRequestCover(TeaModel):
    def __init__(
        self,
        uri: str = None,
    ):
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class UpdateStoryRequest(TeaModel):
    def __init__(
        self,
        cover: UpdateStoryRequestCover = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        dataset_name: str = None,
        object_id: str = None,
        project_name: str = None,
        story_name: str = None,
    ):
        self.cover = cover
        self.custom_id = custom_id
        self.custom_labels = custom_labels
        self.dataset_name = dataset_name
        self.object_id = object_id
        self.project_name = project_name
        self.story_name = story_name

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cover') is not None:
            temp_model = UpdateStoryRequestCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        return self


class UpdateStoryShrinkRequest(TeaModel):
    def __init__(
        self,
        cover_shrink: str = None,
        custom_id: str = None,
        custom_labels_shrink: str = None,
        dataset_name: str = None,
        object_id: str = None,
        project_name: str = None,
        story_name: str = None,
    ):
        self.cover_shrink = cover_shrink
        self.custom_id = custom_id
        self.custom_labels_shrink = custom_labels_shrink
        self.dataset_name = dataset_name
        self.object_id = object_id
        self.project_name = project_name
        self.story_name = story_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_shrink is not None:
            result['Cover'] = self.cover_shrink
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels_shrink is not None:
            result['CustomLabels'] = self.custom_labels_shrink
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cover') is not None:
            self.cover_shrink = m.get('Cover')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels_shrink = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        return self


class UpdateStoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateStoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateStoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


