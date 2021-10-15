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


class Face(TeaModel):
    def __init__(
        self,
        age: int = None,
        age_confidence: float = None,
        beard: str = None,
        beard_confidence: float = None,
        boundary: Boundary = None,
        embeddings_float_32: List[float] = None,
        embeddings_int_8: List[int] = None,
        emotion: str = None,
        emotion_confidence: float = None,
        face_cluster_id: str = None,
        face_confidence: float = None,
        face_id: str = None,
        gender: str = None,
        gender_confidence: float = None,
        glasses: str = None,
        glasses_confidence: float = None,
        hat: str = None,
        hat_confidence: float = None,
        head_pose: HeadPose = None,
        left_eye: str = None,
        left_eye_confidence: float = None,
        mask: str = None,
        mask_confidence: float = None,
        mouth: str = None,
        mouth_confidence: float = None,
        race: str = None,
        race_confidence: float = None,
        right_eye: str = None,
        right_eye_confidence: float = None,
    ):
        # Age
        self.age = age
        # AgeConfidence
        self.age_confidence = age_confidence
        # Beard
        self.beard = beard
        # BeardConfidence
        self.beard_confidence = beard_confidence
        self.boundary = boundary
        # EmbeddingsFloat32
        self.embeddings_float_32 = embeddings_float_32
        # EmbeddingsInt8
        self.embeddings_int_8 = embeddings_int_8
        # Emotion
        self.emotion = emotion
        # EmotionConfidence
        self.emotion_confidence = emotion_confidence
        # FaceClusterId
        self.face_cluster_id = face_cluster_id
        # FaceConfidence
        self.face_confidence = face_confidence
        # FaceId
        self.face_id = face_id
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
        # LeftEye
        self.left_eye = left_eye
        # LeftEyeConfidence
        self.left_eye_confidence = left_eye_confidence
        # Mask
        self.mask = mask
        # MaskConfidence
        self.mask_confidence = mask_confidence
        # Mouth
        self.mouth = mouth
        # MouthConfidence
        self.mouth_confidence = mouth_confidence
        # Race
        self.race = race
        # RaceConfidence
        self.race_confidence = race_confidence
        # RightEye
        self.right_eye = right_eye
        # RightEyeConfidence
        self.right_eye_confidence = right_eye_confidence

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
        if self.age_confidence is not None:
            result['AgeConfidence'] = self.age_confidence
        if self.beard is not None:
            result['Beard'] = self.beard
        if self.beard_confidence is not None:
            result['BeardConfidence'] = self.beard_confidence
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.embeddings_float_32 is not None:
            result['EmbeddingsFloat32'] = self.embeddings_float_32
        if self.embeddings_int_8 is not None:
            result['EmbeddingsInt8'] = self.embeddings_int_8
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.emotion_confidence is not None:
            result['EmotionConfidence'] = self.emotion_confidence
        if self.face_cluster_id is not None:
            result['FaceClusterId'] = self.face_cluster_id
        if self.face_confidence is not None:
            result['FaceConfidence'] = self.face_confidence
        if self.face_id is not None:
            result['FaceId'] = self.face_id
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
        if self.left_eye is not None:
            result['LeftEye'] = self.left_eye
        if self.left_eye_confidence is not None:
            result['LeftEyeConfidence'] = self.left_eye_confidence
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.mask_confidence is not None:
            result['MaskConfidence'] = self.mask_confidence
        if self.mouth is not None:
            result['Mouth'] = self.mouth
        if self.mouth_confidence is not None:
            result['MouthConfidence'] = self.mouth_confidence
        if self.race is not None:
            result['Race'] = self.race
        if self.race_confidence is not None:
            result['RaceConfidence'] = self.race_confidence
        if self.right_eye is not None:
            result['RightEye'] = self.right_eye
        if self.right_eye_confidence is not None:
            result['RightEyeConfidence'] = self.right_eye_confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('AgeConfidence') is not None:
            self.age_confidence = m.get('AgeConfidence')
        if m.get('Beard') is not None:
            self.beard = m.get('Beard')
        if m.get('BeardConfidence') is not None:
            self.beard_confidence = m.get('BeardConfidence')
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('EmbeddingsFloat32') is not None:
            self.embeddings_float_32 = m.get('EmbeddingsFloat32')
        if m.get('EmbeddingsInt8') is not None:
            self.embeddings_int_8 = m.get('EmbeddingsInt8')
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('EmotionConfidence') is not None:
            self.emotion_confidence = m.get('EmotionConfidence')
        if m.get('FaceClusterId') is not None:
            self.face_cluster_id = m.get('FaceClusterId')
        if m.get('FaceConfidence') is not None:
            self.face_confidence = m.get('FaceConfidence')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
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
        if m.get('LeftEye') is not None:
            self.left_eye = m.get('LeftEye')
        if m.get('LeftEyeConfidence') is not None:
            self.left_eye_confidence = m.get('LeftEyeConfidence')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('MaskConfidence') is not None:
            self.mask_confidence = m.get('MaskConfidence')
        if m.get('Mouth') is not None:
            self.mouth = m.get('Mouth')
        if m.get('MouthConfidence') is not None:
            self.mouth_confidence = m.get('MouthConfidence')
        if m.get('Race') is not None:
            self.race = m.get('Race')
        if m.get('RaceConfidence') is not None:
            self.race_confidence = m.get('RaceConfidence')
        if m.get('RightEye') is not None:
            self.right_eye = m.get('RightEye')
        if m.get('RightEyeConfidence') is not None:
            self.right_eye_confidence = m.get('RightEyeConfidence')
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
        label_confidence: float = None,
        label_level: int = None,
        label_name: str = None,
        language: str = None,
    ):
        # LabelConfidence
        self.label_confidence = label_confidence
        # LabelLevel
        self.label_level = label_level
        # LabelName
        self.label_name = label_name
        # Language
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_confidence is not None:
            result['LabelConfidence'] = self.label_confidence
        if self.label_level is not None:
            result['LabelLevel'] = self.label_level
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelConfidence') is not None:
            self.label_confidence = m.get('LabelConfidence')
        if m.get('LabelLevel') is not None:
            self.label_level = m.get('LabelLevel')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class SubtitleStream(TeaModel):
    def __init__(
        self,
        content: str = None,
        index: int = None,
        language: str = None,
    ):
        # Content
        self.content = content
        # Index
        self.index = index
        # Language
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.index is not None:
            result['Index'] = self.index
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class VideoStream(TeaModel):
    def __init__(
        self,
        average_frame_rate: float = None,
        bitrate: int = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        display_aspect_ratio: str = None,
        duration: float = None,
        frame_count: int = None,
        frame_rate: float = None,
        has_bframes: str = None,
        height: int = None,
        index: int = None,
        language: str = None,
        level: int = None,
        pixel_format: str = None,
        profile: str = None,
        sample_aspect_ratio: str = None,
        start_time: float = None,
        time_base: str = None,
        width: int = None,
    ):
        # AverageFrameRate
        self.average_frame_rate = average_frame_rate
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
        artists: List[str] = None,
        audio_bitrate: float = None,
        audio_covers: List[Image] = None,
        audio_duration: float = None,
        audio_embeddings_float_32: List[float] = None,
        audio_embeddings_int_8: List[int] = None,
        audio_language: str = None,
        audio_streams: List[AudioStream] = None,
        audio_taken_time: str = None,
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
        document_embeddings_float_32: List[float] = None,
        document_embeddings_int_8: List[int] = None,
        document_language: str = None,
        etag: str = None,
        exif: str = None,
        face_count: int = None,
        faces: List[Face] = None,
        file_access_time: str = None,
        file_create_time: str = None,
        file_hash: str = None,
        file_modified_time: str = None,
        filename: str = None,
        image_embeddings_float_32: List[float] = None,
        image_embeddings_int_8: List[int] = None,
        image_height: int = None,
        image_score: ImageScore = None,
        image_width: int = None,
        labels: List[Label] = None,
        lat_long: str = None,
        media_type: str = None,
        ocrcontents: List[OCRContents] = None,
        ossdelete_marker: str = None,
        ossexpiration: str = None,
        ossobject_type: str = None,
        osstagging: Dict[str, Any] = None,
        osstagging_count: int = None,
        ossuser_meta: Dict[str, Any] = None,
        ossversion_id: str = None,
        object_acl: str = None,
        object_id: str = None,
        object_type: str = None,
        orientation: str = None,
        owner_id: str = None,
        page_count: int = None,
        performer: str = None,
        produce_time: str = None,
        project_name: str = None,
        server_side_data_encryption: str = None,
        server_side_encryption: str = None,
        server_side_encryption_customer_algorithm: str = None,
        server_side_encryption_key_id: str = None,
        size: int = None,
        storage_class: str = None,
        subtitles: List[SubtitleStream] = None,
        timezone: str = None,
        title: str = None,
        travel_cluster_id: str = None,
        uri: str = None,
        update_time: str = None,
        video_bitrate: int = None,
        video_duration: float = None,
        video_embeddings_float_32: List[float] = None,
        video_embeddings_int_8: List[int] = None,
        video_height: int = None,
        video_start_time: float = None,
        video_streams: List[VideoStream] = None,
        video_taken_time: str = None,
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
        # Artists
        self.artists = artists
        # AudioBitrate
        self.audio_bitrate = audio_bitrate
        # AudioCovers
        self.audio_covers = audio_covers
        # AudioDuration
        self.audio_duration = audio_duration
        # AudioEmbeddingsFloat32
        self.audio_embeddings_float_32 = audio_embeddings_float_32
        # AudioEmbeddingsInt8
        self.audio_embeddings_int_8 = audio_embeddings_int_8
        # AudioLanguage
        self.audio_language = audio_language
        # AudioStreams
        self.audio_streams = audio_streams
        # AudioTakenTime
        self.audio_taken_time = audio_taken_time
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
        # DocumentEmbeddingsFloat32
        self.document_embeddings_float_32 = document_embeddings_float_32
        # DocumentEmbeddingsInt8
        self.document_embeddings_int_8 = document_embeddings_int_8
        # DocumentLanguage
        self.document_language = document_language
        # ETag
        self.etag = etag
        # EXIF
        self.exif = exif
        # FaceCount
        self.face_count = face_count
        # Faces
        self.faces = faces
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
        # ImageEmbeddingsFloat32
        self.image_embeddings_float_32 = image_embeddings_float_32
        # ImageEmbeddingsInt8
        self.image_embeddings_int_8 = image_embeddings_int_8
        # ImageHeight
        self.image_height = image_height
        self.image_score = image_score
        # ImageWidth
        self.image_width = image_width
        # Labels
        self.labels = labels
        # LatLong
        self.lat_long = lat_long
        # MediaType
        self.media_type = media_type
        # OCRContents
        self.ocrcontents = ocrcontents
        # OSSDeleteMarker
        self.ossdelete_marker = ossdelete_marker
        # OSSExpiration
        self.ossexpiration = ossexpiration
        # OSSObjectType
        self.ossobject_type = ossobject_type
        # OSSTagging
        self.osstagging = osstagging
        # OSSTaggingCount
        self.osstagging_count = osstagging_count
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
        # StorageClass
        self.storage_class = storage_class
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
        # VideoBitrate
        self.video_bitrate = video_bitrate
        # VideoDuration
        self.video_duration = video_duration
        # VideoEmbeddingsFloat32
        self.video_embeddings_float_32 = video_embeddings_float_32
        # VideoEmbeddingsInt8
        self.video_embeddings_int_8 = video_embeddings_int_8
        # VideoHeight
        self.video_height = video_height
        # VideoStartTime
        self.video_start_time = video_start_time
        # VideoStreams
        self.video_streams = video_streams
        # VideoTakenTime
        self.video_taken_time = video_taken_time
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
        if self.faces:
            for k in self.faces:
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
        if self.artists is not None:
            result['Artists'] = self.artists
        if self.audio_bitrate is not None:
            result['AudioBitrate'] = self.audio_bitrate
        result['AudioCovers'] = []
        if self.audio_covers is not None:
            for k in self.audio_covers:
                result['AudioCovers'].append(k.to_map() if k else None)
        if self.audio_duration is not None:
            result['AudioDuration'] = self.audio_duration
        if self.audio_embeddings_float_32 is not None:
            result['AudioEmbeddingsFloat32'] = self.audio_embeddings_float_32
        if self.audio_embeddings_int_8 is not None:
            result['AudioEmbeddingsInt8'] = self.audio_embeddings_int_8
        if self.audio_language is not None:
            result['AudioLanguage'] = self.audio_language
        result['AudioStreams'] = []
        if self.audio_streams is not None:
            for k in self.audio_streams:
                result['AudioStreams'].append(k.to_map() if k else None)
        if self.audio_taken_time is not None:
            result['AudioTakenTime'] = self.audio_taken_time
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
        if self.document_embeddings_float_32 is not None:
            result['DocumentEmbeddingsFloat32'] = self.document_embeddings_float_32
        if self.document_embeddings_int_8 is not None:
            result['DocumentEmbeddingsInt8'] = self.document_embeddings_int_8
        if self.document_language is not None:
            result['DocumentLanguage'] = self.document_language
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.exif is not None:
            result['EXIF'] = self.exif
        if self.face_count is not None:
            result['FaceCount'] = self.face_count
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
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
        if self.image_embeddings_float_32 is not None:
            result['ImageEmbeddingsFloat32'] = self.image_embeddings_float_32
        if self.image_embeddings_int_8 is not None:
            result['ImageEmbeddingsInt8'] = self.image_embeddings_int_8
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
        if self.lat_long is not None:
            result['LatLong'] = self.lat_long
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        result['OCRContents'] = []
        if self.ocrcontents is not None:
            for k in self.ocrcontents:
                result['OCRContents'].append(k.to_map() if k else None)
        if self.ossdelete_marker is not None:
            result['OSSDeleteMarker'] = self.ossdelete_marker
        if self.ossexpiration is not None:
            result['OSSExpiration'] = self.ossexpiration
        if self.ossobject_type is not None:
            result['OSSObjectType'] = self.ossobject_type
        if self.osstagging is not None:
            result['OSSTagging'] = self.osstagging
        if self.osstagging_count is not None:
            result['OSSTaggingCount'] = self.osstagging_count
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
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
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
        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate
        if self.video_duration is not None:
            result['VideoDuration'] = self.video_duration
        if self.video_embeddings_float_32 is not None:
            result['VideoEmbeddingsFloat32'] = self.video_embeddings_float_32
        if self.video_embeddings_int_8 is not None:
            result['VideoEmbeddingsInt8'] = self.video_embeddings_int_8
        if self.video_height is not None:
            result['VideoHeight'] = self.video_height
        if self.video_start_time is not None:
            result['VideoStartTime'] = self.video_start_time
        result['VideoStreams'] = []
        if self.video_streams is not None:
            for k in self.video_streams:
                result['VideoStreams'].append(k.to_map() if k else None)
        if self.video_taken_time is not None:
            result['VideoTakenTime'] = self.video_taken_time
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
        if m.get('Artists') is not None:
            self.artists = m.get('Artists')
        if m.get('AudioBitrate') is not None:
            self.audio_bitrate = m.get('AudioBitrate')
        self.audio_covers = []
        if m.get('AudioCovers') is not None:
            for k in m.get('AudioCovers'):
                temp_model = Image()
                self.audio_covers.append(temp_model.from_map(k))
        if m.get('AudioDuration') is not None:
            self.audio_duration = m.get('AudioDuration')
        if m.get('AudioEmbeddingsFloat32') is not None:
            self.audio_embeddings_float_32 = m.get('AudioEmbeddingsFloat32')
        if m.get('AudioEmbeddingsInt8') is not None:
            self.audio_embeddings_int_8 = m.get('AudioEmbeddingsInt8')
        if m.get('AudioLanguage') is not None:
            self.audio_language = m.get('AudioLanguage')
        self.audio_streams = []
        if m.get('AudioStreams') is not None:
            for k in m.get('AudioStreams'):
                temp_model = AudioStream()
                self.audio_streams.append(temp_model.from_map(k))
        if m.get('AudioTakenTime') is not None:
            self.audio_taken_time = m.get('AudioTakenTime')
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
        if m.get('DocumentEmbeddingsFloat32') is not None:
            self.document_embeddings_float_32 = m.get('DocumentEmbeddingsFloat32')
        if m.get('DocumentEmbeddingsInt8') is not None:
            self.document_embeddings_int_8 = m.get('DocumentEmbeddingsInt8')
        if m.get('DocumentLanguage') is not None:
            self.document_language = m.get('DocumentLanguage')
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('EXIF') is not None:
            self.exif = m.get('EXIF')
        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = Face()
                self.faces.append(temp_model.from_map(k))
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
        if m.get('ImageEmbeddingsFloat32') is not None:
            self.image_embeddings_float_32 = m.get('ImageEmbeddingsFloat32')
        if m.get('ImageEmbeddingsInt8') is not None:
            self.image_embeddings_int_8 = m.get('ImageEmbeddingsInt8')
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
        if m.get('LatLong') is not None:
            self.lat_long = m.get('LatLong')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        self.ocrcontents = []
        if m.get('OCRContents') is not None:
            for k in m.get('OCRContents'):
                temp_model = OCRContents()
                self.ocrcontents.append(temp_model.from_map(k))
        if m.get('OSSDeleteMarker') is not None:
            self.ossdelete_marker = m.get('OSSDeleteMarker')
        if m.get('OSSExpiration') is not None:
            self.ossexpiration = m.get('OSSExpiration')
        if m.get('OSSObjectType') is not None:
            self.ossobject_type = m.get('OSSObjectType')
        if m.get('OSSTagging') is not None:
            self.osstagging = m.get('OSSTagging')
        if m.get('OSSTaggingCount') is not None:
            self.osstagging_count = m.get('OSSTaggingCount')
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
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
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
        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')
        if m.get('VideoDuration') is not None:
            self.video_duration = m.get('VideoDuration')
        if m.get('VideoEmbeddingsFloat32') is not None:
            self.video_embeddings_float_32 = m.get('VideoEmbeddingsFloat32')
        if m.get('VideoEmbeddingsInt8') is not None:
            self.video_embeddings_int_8 = m.get('VideoEmbeddingsInt8')
        if m.get('VideoHeight') is not None:
            self.video_height = m.get('VideoHeight')
        if m.get('VideoStartTime') is not None:
            self.video_start_time = m.get('VideoStartTime')
        self.video_streams = []
        if m.get('VideoStreams') is not None:
            for k in m.get('VideoStreams'):
                temp_model = VideoStream()
                self.video_streams.append(temp_model.from_map(k))
        if m.get('VideoTakenTime') is not None:
            self.video_taken_time = m.get('VideoTakenTime')
        if m.get('VideoWidth') is not None:
            self.video_width = m.get('VideoWidth')
        return self


class FileForReq(TeaModel):
    def __init__(
        self,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        file_hash: str = None,
        ossuri: str = None,
        uri: str = None,
    ):
        # CustomId
        self.custom_id = custom_id
        # CustomLabels
        self.custom_labels = custom_labels
        # FileHash
        self.file_hash = file_hash
        # OSSURI
        self.ossuri = ossuri
        # URI
        self.uri = uri

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
        if self.file_hash is not None:
            result['FileHash'] = self.file_hash
        if self.ossuri is not None:
            result['OSSURI'] = self.ossuri
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')
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


class OfficeConversionTask(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        end_time: str = None,
        reason: str = None,
        start_time: str = None,
        status: str = None,
        task_id: str = None,
        total_pages: int = None,
        user_data: str = None,
    ):
        # 任务创建时间
        self.create_time = create_time
        # 任务解释时间
        self.end_time = end_time
        # Status 解释
        self.reason = reason
        # 任务开始时间
        self.start_time = start_time
        # 任务状态
        self.status = status
        # 任务 id
        self.task_id = task_id
        # 转换页数
        self.total_pages = total_pages
        # 用户自定义内容
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
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


class BatchDeleteFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
        uris: List[str] = None,
    ):
        self.dataset_name = dataset_name
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
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
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uris is not None:
            result['URIs'] = self.uris
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
        if m.get('URIs') is not None:
            self.uris = m.get('URIs')
        return self


class BatchDeleteFileMetaShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
        uris_shrink: str = None,
    ):
        self.dataset_name = dataset_name
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
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
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uris_shrink is not None:
            result['URIs'] = self.uris_shrink
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
        if m.get('URIs') is not None:
            self.uris_shrink = m.get('URIs')
        return self


class BatchDeleteFileMetaResponseBody(TeaModel):
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


class BatchDeleteFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchDeleteFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: BatchGetFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: BatchIndexFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchIndexFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUpdateFileMetaRequest(TeaModel):
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


class BatchUpdateFileMetaShrinkRequest(TeaModel):
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


class BatchUpdateFileMetaResponseBody(TeaModel):
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


class BatchUpdateFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchUpdateFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: CreateBindingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: CreateDatasetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOfficeConversionTaskRequest(TeaModel):
    def __init__(
        self,
        end_page: str = None,
        first_page: bool = None,
        fit_to_height: bool = None,
        fit_to_width: bool = None,
        is_horizontal: bool = None,
        long_pic: bool = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        paper_size: str = None,
        password: str = None,
        project_name: str = None,
        quality: int = None,
        scale: int = None,
        sheet_count: str = None,
        sheet_index: int = None,
        show_comments: bool = None,
        source_type: str = None,
        source_uri: str = None,
        start_page: str = None,
        target_type: str = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        # 结束转换页，如果是 excel 需要指定 SheetIndex
        self.end_page = end_page
        # 表格转图片参数，只返回表格的第一张图片，图片包含的行数列数是自动切割的结果。必须在LongPic为true的情况下才有效。默认为false
        self.first_page = first_page
        # 表格转图片，所有行输出到一张图片
        self.fit_to_height = fit_to_height
        # 表格转图片，所有列输出到一张图片
        self.fit_to_width = fit_to_width
        # 水平放置纸张，默认 false
        self.is_horizontal = is_horizontal
        # 转图片，合成一个一张产长图，最多20张图片，默认 false
        self.long_pic = long_pic
        # mns 消息地址
        self.notify_endpoint = notify_endpoint
        # mns 消息 topic
        self.notify_topic_name = notify_topic_name
        # 纸张大小 A4, A2, A0，默认 A4
        self.paper_size = paper_size
        self.password = password
        # 项目名称
        self.project_name = project_name
        # 转化质量0~100
        self.quality = quality
        # 缩放大小 20~200，默认100，小于100缩放，大于100放大
        self.scale = scale
        # excel 转换 sheet 的数量，默认转换所有
        self.sheet_count = sheet_count
        # excel 标签页，从 1 开始
        self.sheet_index = sheet_index
        # 显示批注
        self.show_comments = show_comments
        self.source_type = source_type
        self.source_uri = source_uri
        # 开始转换页，如果是 excel 需要指定 SheetIndex
        self.start_page = start_page
        self.target_type = target_type
        self.target_uri = target_uri
        # 用户自定义信息，此信息将在 Task 中回传
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_page is not None:
            result['EndPage'] = self.end_page
        if self.first_page is not None:
            result['FirstPage'] = self.first_page
        if self.fit_to_height is not None:
            result['FitToHeight'] = self.fit_to_height
        if self.fit_to_width is not None:
            result['FitToWidth'] = self.fit_to_width
        if self.is_horizontal is not None:
            result['IsHorizontal'] = self.is_horizontal
        if self.long_pic is not None:
            result['LongPic'] = self.long_pic
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.paper_size is not None:
            result['PaperSize'] = self.paper_size
        if self.password is not None:
            result['Password'] = self.password
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.scale is not None:
            result['Scale'] = self.scale
        if self.sheet_count is not None:
            result['SheetCount'] = self.sheet_count
        if self.sheet_index is not None:
            result['SheetIndex'] = self.sheet_index
        if self.show_comments is not None:
            result['ShowComments'] = self.show_comments
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.start_page is not None:
            result['StartPage'] = self.start_page
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.target_uri is not None:
            result['TargetUri'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndPage') is not None:
            self.end_page = m.get('EndPage')
        if m.get('FirstPage') is not None:
            self.first_page = m.get('FirstPage')
        if m.get('FitToHeight') is not None:
            self.fit_to_height = m.get('FitToHeight')
        if m.get('FitToWidth') is not None:
            self.fit_to_width = m.get('FitToWidth')
        if m.get('IsHorizontal') is not None:
            self.is_horizontal = m.get('IsHorizontal')
        if m.get('LongPic') is not None:
            self.long_pic = m.get('LongPic')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('PaperSize') is not None:
            self.paper_size = m.get('PaperSize')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('Scale') is not None:
            self.scale = m.get('Scale')
        if m.get('SheetCount') is not None:
            self.sheet_count = m.get('SheetCount')
        if m.get('SheetIndex') is not None:
            self.sheet_index = m.get('SheetIndex')
        if m.get('ShowComments') is not None:
            self.show_comments = m.get('ShowComments')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('StartPage') is not None:
            self.start_page = m.get('StartPage')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TargetUri') is not None:
            self.target_uri = m.get('TargetUri')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateOfficeConversionTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
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


class CreateOfficeConversionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateOfficeConversionTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: CreateProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBindingRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        project_name: str = None,
        uri: str = None,
    ):
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
        body: DeleteBindingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DeleteDatasetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_name: str = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
        uri: str = None,
    ):
        self.dataset_name = dataset_name
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
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
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
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
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class DeleteFileMetaResponseBody(TeaModel):
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


class DeleteFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DeleteProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageLabelsRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        source_uri: str = None,
        threshold: float = None,
    ):
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
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        body: DetectImageLabelsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetectImageLabelsResponseBody()
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
        body: FuzzyQueryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: GetBindingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: GetDatasetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDatasetResponseBody()
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
        body: GetFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileSignedURIRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        uri: str = None,
    ):
        self.project_name = project_name
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GetFileSignedURIResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        uri: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 签名地址
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GetFileSignedURIResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFileSignedURIResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetFileSignedURIResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOfficeConversionTaskRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        task_id: str = None,
    ):
        # 项目名称
        self.project_name = project_name
        # 任务 id
        self.task_id = task_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetOfficeConversionTaskResponseBody(TeaModel):
    def __init__(
        self,
        office_conversion_task: OfficeConversionTask = None,
        request_id: str = None,
    ):
        self.office_conversion_task = office_conversion_task
        self.request_id = request_id

    def validate(self):
        if self.office_conversion_task:
            self.office_conversion_task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.office_conversion_task is not None:
            result['OfficeConversionTask'] = self.office_conversion_task.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfficeConversionTask') is not None:
            temp_model = OfficeConversionTask()
            self.office_conversion_task = temp_model.from_map(m['OfficeConversionTask'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOfficeConversionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOfficeConversionTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetOfficeConversionTaskResponseBody()
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
        body: GetProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebofficeURLRequest(TeaModel):
    def __init__(
        self,
        assume_role_chain: AssumeRoleChain = None,
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
        # 链式授权
        self.assume_role_chain = assume_role_chain
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
        if self.assume_role_chain:
            self.assume_role_chain.validate()
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
        if self.assume_role_chain is not None:
            result['AssumeRoleChain'] = self.assume_role_chain.to_map()
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
        if m.get('AssumeRoleChain') is not None:
            temp_model = AssumeRoleChain()
            self.assume_role_chain = temp_model.from_map(m['AssumeRoleChain'])
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
        assume_role_chain_shrink: str = None,
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
        # 链式授权
        self.assume_role_chain_shrink = assume_role_chain_shrink
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
        if self.assume_role_chain_shrink is not None:
            result['AssumeRoleChain'] = self.assume_role_chain_shrink
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
        if m.get('AssumeRoleChain') is not None:
            self.assume_role_chain_shrink = m.get('AssumeRoleChain')
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
        body: GetWebofficeURLResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: IndexFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: ListBindingsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: ListDatasetsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDatasetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOfficeConversionTaskRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        project_name: str = None,
    ):
        # 最大结果数
        self.max_results = max_results
        # 下一条记录开始标记
        self.next_token = next_token
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
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ListOfficeConversionTaskResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        office_conversion_tasks: List[OfficeConversionTask] = None,
        request_id: str = None,
    ):
        self.next_token = next_token
        self.office_conversion_tasks = office_conversion_tasks
        self.request_id = request_id

    def validate(self):
        if self.office_conversion_tasks:
            for k in self.office_conversion_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['OfficeConversionTasks'] = []
        if self.office_conversion_tasks is not None:
            for k in self.office_conversion_tasks:
                result['OfficeConversionTasks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.office_conversion_tasks = []
        if m.get('OfficeConversionTasks') is not None:
            for k in m.get('OfficeConversionTasks'):
                temp_model = OfficeConversionTask()
                self.office_conversion_tasks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListOfficeConversionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOfficeConversionTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListOfficeConversionTaskResponseBody()
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
        body: ListProjectsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshWebofficeTokenRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        assume_role_chain: AssumeRoleChain = None,
        project_name: str = None,
        refresh_token: str = None,
    ):
        # access token
        self.access_token = access_token
        # 链式授权
        self.assume_role_chain = assume_role_chain
        # 项目名称
        self.project_name = project_name
        # refresh token
        self.refresh_token = refresh_token

    def validate(self):
        if self.assume_role_chain:
            self.assume_role_chain.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.assume_role_chain is not None:
            result['AssumeRoleChain'] = self.assume_role_chain.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AssumeRoleChain') is not None:
            temp_model = AssumeRoleChain()
            self.assume_role_chain = temp_model.from_map(m['AssumeRoleChain'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        return self


class RefreshWebofficeTokenShrinkRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        assume_role_chain_shrink: str = None,
        project_name: str = None,
        refresh_token: str = None,
    ):
        # access token
        self.access_token = access_token
        # 链式授权
        self.assume_role_chain_shrink = assume_role_chain_shrink
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
        if self.assume_role_chain_shrink is not None:
            result['AssumeRoleChain'] = self.assume_role_chain_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AssumeRoleChain') is not None:
            self.assume_role_chain_shrink = m.get('AssumeRoleChain')
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
        body: RefreshWebofficeTokenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RefreshWebofficeTokenResponseBody()
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
        body: ResumeBindingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResumeBindingResponseBody()
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
        return self


class SimpleQueryResponseBodyAggregationsGroups(TeaModel):
    def __init__(
        self,
        value: str = None,
        count: int = None,
    ):
        # 分组聚合的值
        self.value = value
        # 分组聚合的计数
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class SimpleQueryResponseBodyAggregations(TeaModel):
    def __init__(
        self,
        field: str = None,
        operation: str = None,
        value: float = None,
        groups: List[SimpleQueryResponseBodyAggregationsGroups] = None,
    ):
        # 聚合字段名
        self.field = field
        # 聚合字段的聚合操作符
        self.operation = operation
        # 聚合的统计结果
        self.value = value
        # 分组聚合的结果
        self.groups = groups

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
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.value is not None:
            result['Value'] = self.value
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = SimpleQueryResponseBodyAggregationsGroups()
                self.groups.append(temp_model.from_map(k))
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
        body: SimpleQueryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: StopBindingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: UpdateDatasetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFileMetaRequest(TeaModel):
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


class UpdateFileMetaShrinkRequest(TeaModel):
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


class UpdateFileMetaResponseBody(TeaModel):
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


class UpdateFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFileMetaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: UpdateProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


