# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class File(DaraModel):
    def __init__(
        self,
        access_control_allow_origin: str = None,
        access_control_request_method: str = None,
        addresses: List[main_models.Address] = None,
        album: str = None,
        album_artist: str = None,
        artist: str = None,
        audio_covers: List[main_models.Image] = None,
        audio_streams: List[main_models.AudioStream] = None,
        bitrate: int = None,
        cache_control: str = None,
        composer: str = None,
        content_disposition: str = None,
        content_encoding: str = None,
        content_language: str = None,
        content_md_5: str = None,
        content_type: str = None,
        create_time: str = None,
        cropping_suggestions: List[main_models.CroppingSuggestion] = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        dataset_name: str = None,
        duration: float = None,
        etag: str = None,
        exif: str = None,
        elements: List[main_models.Element] = None,
        figure_count: int = None,
        figures: List[main_models.Figure] = None,
        file_access_time: str = None,
        file_create_time: str = None,
        file_hash: str = None,
        file_modified_time: str = None,
        filename: str = None,
        format_long_name: str = None,
        format_name: str = None,
        image_height: int = None,
        image_score: main_models.ImageScore = None,
        image_width: int = None,
        insights: main_models.Insights = None,
        labels: List[main_models.Label] = None,
        language: str = None,
        lat_long: str = None,
        media_type: str = None,
        ocrcontents: List[main_models.OCRContents] = None,
        ocrtexts: str = None,
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
        object_status: str = None,
        object_type: str = None,
        orientation: int = None,
        owner_id: str = None,
        page_count: int = None,
        performer: str = None,
        produce_time: str = None,
        program_count: int = None,
        project_name: str = None,
        reason: str = None,
        scene_elements: List[main_models.SceneElement] = None,
        semantic_types: List[str] = None,
        server_side_data_encryption: str = None,
        server_side_encryption: str = None,
        server_side_encryption_customer_algorithm: str = None,
        server_side_encryption_key_id: str = None,
        size: int = None,
        start_time: float = None,
        stream_count: int = None,
        subtitles: List[main_models.SubtitleStream] = None,
        timezone: str = None,
        title: str = None,
        travel_cluster_id: str = None,
        uri: str = None,
        update_time: str = None,
        video_height: int = None,
        video_streams: List[main_models.VideoStream] = None,
        video_width: int = None,
    ):
        # The origin allowed in cross-origin requests.
        self.access_control_allow_origin = access_control_allow_origin
        # The method to be used in the actual cross-origin request.
        self.access_control_request_method = access_control_request_method
        # The addresses.
        self.addresses = addresses
        # The album.
        self.album = album
        # The singer.
        self.album_artist = album_artist
        # The artist.
        self.artist = artist
        # The audio covers.
        self.audio_covers = audio_covers
        # The list of audio streams.
        self.audio_streams = audio_streams
        # The bitrate. Unit: bit/s.
        self.bitrate = bitrate
        # The caching behavior of the web page when the object is downloaded.
        # 
        # This parameter corresponds to the Cache-Control HTTP header of the OSS object. For more information, see [Manage object metadata](https://help.aliyun.com/document_detail/31859.html).
        self.cache_control = cache_control
        # The composer.
        self.composer = composer
        # The name of the object during the download.
        # 
        # This parameter corresponds to the Content-Disposition HTTP header of the OSS object. For more information, see [Manage object metadata](https://help.aliyun.com/document_detail/31859.html).
        self.content_disposition = content_disposition
        # The content encoding format of the object when the object is downloaded.
        # 
        # This parameter corresponds to the Content-Encoding HTTP header of the OSS object. For more information, see [Manage object metadata](https://help.aliyun.com/document_detail/31859.html).
        self.content_encoding = content_encoding
        # The language of the object content.
        # 
        # This parameter corresponds to the Content-Language HTTP header of the OSS object. For more information, see [Manage object metadata](https://help.aliyun.com/document_detail/31859.html).
        self.content_language = content_language
        # The MD5 value.
        self.content_md_5 = content_md_5
        # The Multipurpose Internet Mail Extensions (MIME) type of the file.
        self.content_type = content_type
        # The RFC3339Nano timestamp when the metadata was created.
        self.create_time = create_time
        # The cropping suggestions for the image.
        # 
        # > Not supported.
        self.cropping_suggestions = cropping_suggestions
        # The custom ID of the file. When the cluster is indexed into the dataset, the custom ID is stored as the data attribute. You can map the custom ID to other data in your business system. Configure this parameter based on your business requirements. For example, you can associate a URI with an ID in your system. We recommend that you set this parameter to a globally unique value.
        self.custom_id = custom_id
        # The custom labels of the file. This parameter is optional. The parameter stores custom key-value labels, which can be used to filter data.
        self.custom_labels = custom_labels
        # The name of the dataset. You can obtain the name of the dataset from the response of the [CreateDataset](https://help.aliyun.com/document_detail/478160.html) operation.
        self.dataset_name = dataset_name
        # The total duration of the video. Unit: seconds.
        self.duration = duration
        # The ETag of the object. ETags are used to identify the content of objects.
        self.etag = etag
        # The original EXIF information about the image. The EXIF information is stored in the serialized JSON format. For more information, see [Query image information](https://help.aliyun.com/document_detail/44975.html).
        self.exif = exif
        # The document elements that match the current query content when you call the SemanticQuery operation for semantic search.
        self.elements = elements
        # The number of persons.
        self.figure_count = figure_count
        # The list of persons. The persons are detected via AI models.
        self.figures = figures
        # The RFC3339Nano timestamp when the file was accessed.
        self.file_access_time = file_access_time
        # The RFC3339Nano timestamp when the file was created.
        self.file_create_time = file_create_time
        # The hash value of the file.
        self.file_hash = file_hash
        # The RFC3339Nano timestamp when the file was last modified.
        self.file_modified_time = file_modified_time
        # The name of the object. For an OSS object, the value of this parameter is the object name.
        self.filename = filename
        # The full name of the media format.
        self.format_long_name = format_long_name
        # The name of the media format.
        self.format_name = format_name
        # The height of the image. Unit: pixels.
        self.image_height = image_height
        # The score of the image. The score is calculated by using AI models.
        self.image_score = image_score
        # The width of the image. Unit: pixels.
        self.image_width = image_width
        # Summary and description of the file.
        # 
        # > Not supported.
        self.insights = insights
        # The labels of the file. The labels are detected via AI models.
        self.labels = labels
        # The language specified by using a BCP 47 language tag.
        self.language = language
        # The latitude and longitude.
        self.lat_long = lat_long
        # The media type of the file.
        # 
        # Valid values:
        # 
        # *   image
        # *   other
        # *   document
        # *   archive
        # *   audio
        # *   video
        self.media_type = media_type
        # The Optical Character Recognition (OCR) results.
        # 
        # > Not supported.
        self.ocrcontents = ocrcontents
        # The text detected in the image.
        self.ocrtexts = ocrtexts
        # The CRC64 value.
        self.osscrc64 = osscrc64
        # The delete marker of the object.
        self.ossdelete_marker = ossdelete_marker
        # The expiration time of the OSS object.
        # 
        # This parameter corresponds to the Expires HTTP header of the OSS object. For more information, see [Manage object metadata](https://help.aliyun.com/document_detail/31859.html).
        self.ossexpiration = ossexpiration
        # The type of the OSS object. Set the value to `Normal`.
        self.ossobject_type = ossobject_type
        # The storage class of the OSS bucket.
        self.ossstorage_class = ossstorage_class
        # The tag of the object.
        # 
        # For more information, see [Add tags to an object](https://help.aliyun.com/document_detail/106678.html).
        self.osstagging = osstagging
        # The number of OSS object tags.
        # 
        # This parameter is available only if tags are added to the corresponding OSS object. For more information, see [Add tags to an object](https://help.aliyun.com/document_detail/106678.html).
        self.osstagging_count = osstagging_count
        # The URI of the OSS object. This parameter is available only if the value of the URI parameter is the URI of a file in Photo and Drive Service.
        self.ossuri = ossuri
        # The user metadata of the OSS object.
        # 
        # This parameter is available only if user metadata is configured for the OSS object. For more information, see [Manage object metadata](https://help.aliyun.com/document_detail/31859.html).
        self.ossuser_meta = ossuser_meta
        # The version of the object.
        # 
        # This parameter is available only if versioning is enabled for the bucket. For more information, see [Overview](https://help.aliyun.com/document_detail/109695.html).
        self.ossversion_id = ossversion_id
        # The access control list (ACL) of the OSS object.
        self.object_acl = object_acl
        # The unique ID of the object.
        self.object_id = object_id
        # The status of the object.
        self.object_status = object_status
        # The type of the object. Set the value to **file**.
        self.object_type = object_type
        # The image rotation angle. You can obtain the value from the exchangeable image file format (EXIF).
        # 
        # If the EXIF metadata does not contain the image rotation angle, this parameter is not included in the response.
        self.orientation = orientation
        # The ID of the Alibaba Cloud account.
        self.owner_id = owner_id
        # The number of pages.
        # 
        # > Not supported.
        self.page_count = page_count
        # The performer.
        self.performer = performer
        # The time when the image was taken.
        self.produce_time = produce_time
        # The number of programs in the media container.
        self.program_count = program_count
        # The name of the project. You can obtain the name of the project from the response of the [CreateProject](https://help.aliyun.com/document_detail/478153.html) operation.
        self.project_name = project_name
        # The reason why the file failed to run the index.
        self.reason = reason
        # The elements in the video segment, which are scene elements that you can extract from the video by using an AI model.
        self.scene_elements = scene_elements
        # The reasons for which the current file is included in the search results when you call the SemanticQuery operation for semantic search.
        self.semantic_types = semantic_types
        # The encryption method of the object.
        # 
        # This parameter is available only if server encryption is configured for the OSS bucket. For more information, see [Server-side encryption](https://help.aliyun.com/document_detail/31871.html).
        self.server_side_data_encryption = server_side_data_encryption
        # The encryption method on the server side.
        # 
        # This parameter is available only if server encryption is configured for the OSS bucket. For more information, see [Server-side encryption](https://help.aliyun.com/document_detail/31871.html).
        self.server_side_encryption = server_side_encryption
        # The algorithm that is used to encrypt the file on the server side.
        self.server_side_encryption_customer_algorithm = server_side_encryption_customer_algorithm
        # The ID of the customer master key (CMK) managed by Key Management Service (KMS).
        # 
        # This parameter is available only if server encryption is configured for the OSS bucket. For more information, see [Server-side encryption](https://help.aliyun.com/document_detail/31871.html).
        self.server_side_encryption_key_id = server_side_encryption_key_id
        # The size of the object. Unit: bytes.
        self.size = size
        # The time of the first frame. Unit: seconds.
        self.start_time = start_time
        # The number of media streams in the media container.
        self.stream_count = stream_count
        # The list of subtitle streams.
        self.subtitles = subtitles
        # The time zone.
        # 
        # >  Not supported.
        self.timezone = timezone
        # The title of the file.
        self.title = title
        # A reserved parameter.
        # 
        # > Not supported.
        self.travel_cluster_id = travel_cluster_id
        # The URI of the file.
        # 
        # The URI of an OSS object follows the oss://${Bucket}/${Object} format, where `${Bucket}` is the name of the bucket in the same region as the current project and `${Object}` is the path of the object with the extension included.
        # 
        # The URI of a file in Photo and Drive Service follows the pds://domains/${domain}/drives/${drive}/files/${file}/revisions/${revision} format.
        self.uri = uri
        # The RFC3339Nano timestamp when the metadata was modified.
        self.update_time = update_time
        # The height of the video. Unit: pixels.
        self.video_height = video_height
        # The list of video streams.
        self.video_streams = video_streams
        # The width of the video. Unit: pixels.
        self.video_width = video_width

    def validate(self):
        if self.addresses:
            for v1 in self.addresses:
                 if v1:
                    v1.validate()
        if self.audio_covers:
            for v1 in self.audio_covers:
                 if v1:
                    v1.validate()
        if self.audio_streams:
            for v1 in self.audio_streams:
                 if v1:
                    v1.validate()
        if self.cropping_suggestions:
            for v1 in self.cropping_suggestions:
                 if v1:
                    v1.validate()
        if self.elements:
            for v1 in self.elements:
                 if v1:
                    v1.validate()
        if self.figures:
            for v1 in self.figures:
                 if v1:
                    v1.validate()
        if self.image_score:
            self.image_score.validate()
        if self.insights:
            self.insights.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.ocrcontents:
            for v1 in self.ocrcontents:
                 if v1:
                    v1.validate()
        if self.scene_elements:
            for v1 in self.scene_elements:
                 if v1:
                    v1.validate()
        if self.subtitles:
            for v1 in self.subtitles:
                 if v1:
                    v1.validate()
        if self.video_streams:
            for v1 in self.video_streams:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_control_allow_origin is not None:
            result['AccessControlAllowOrigin'] = self.access_control_allow_origin

        if self.access_control_request_method is not None:
            result['AccessControlRequestMethod'] = self.access_control_request_method

        result['Addresses'] = []
        if self.addresses is not None:
            for k1 in self.addresses:
                result['Addresses'].append(k1.to_map() if k1 else None)

        if self.album is not None:
            result['Album'] = self.album

        if self.album_artist is not None:
            result['AlbumArtist'] = self.album_artist

        if self.artist is not None:
            result['Artist'] = self.artist

        result['AudioCovers'] = []
        if self.audio_covers is not None:
            for k1 in self.audio_covers:
                result['AudioCovers'].append(k1.to_map() if k1 else None)

        result['AudioStreams'] = []
        if self.audio_streams is not None:
            for k1 in self.audio_streams:
                result['AudioStreams'].append(k1.to_map() if k1 else None)

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
            for k1 in self.cropping_suggestions:
                result['CroppingSuggestions'].append(k1.to_map() if k1 else None)

        if self.custom_id is not None:
            result['CustomId'] = self.custom_id

        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.etag is not None:
            result['ETag'] = self.etag

        if self.exif is not None:
            result['EXIF'] = self.exif

        result['Elements'] = []
        if self.elements is not None:
            for k1 in self.elements:
                result['Elements'].append(k1.to_map() if k1 else None)

        if self.figure_count is not None:
            result['FigureCount'] = self.figure_count

        result['Figures'] = []
        if self.figures is not None:
            for k1 in self.figures:
                result['Figures'].append(k1.to_map() if k1 else None)

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

        if self.insights is not None:
            result['Insights'] = self.insights.to_map()

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.language is not None:
            result['Language'] = self.language

        if self.lat_long is not None:
            result['LatLong'] = self.lat_long

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        result['OCRContents'] = []
        if self.ocrcontents is not None:
            for k1 in self.ocrcontents:
                result['OCRContents'].append(k1.to_map() if k1 else None)

        if self.ocrtexts is not None:
            result['OCRTexts'] = self.ocrtexts

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

        if self.object_status is not None:
            result['ObjectStatus'] = self.object_status

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

        if self.reason is not None:
            result['Reason'] = self.reason

        result['SceneElements'] = []
        if self.scene_elements is not None:
            for k1 in self.scene_elements:
                result['SceneElements'].append(k1.to_map() if k1 else None)

        if self.semantic_types is not None:
            result['SemanticTypes'] = self.semantic_types

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
            for k1 in self.subtitles:
                result['Subtitles'].append(k1.to_map() if k1 else None)

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
            for k1 in self.video_streams:
                result['VideoStreams'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('Addresses'):
                temp_model = main_models.Address()
                self.addresses.append(temp_model.from_map(k1))

        if m.get('Album') is not None:
            self.album = m.get('Album')

        if m.get('AlbumArtist') is not None:
            self.album_artist = m.get('AlbumArtist')

        if m.get('Artist') is not None:
            self.artist = m.get('Artist')

        self.audio_covers = []
        if m.get('AudioCovers') is not None:
            for k1 in m.get('AudioCovers'):
                temp_model = main_models.Image()
                self.audio_covers.append(temp_model.from_map(k1))

        self.audio_streams = []
        if m.get('AudioStreams') is not None:
            for k1 in m.get('AudioStreams'):
                temp_model = main_models.AudioStream()
                self.audio_streams.append(temp_model.from_map(k1))

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
            for k1 in m.get('CroppingSuggestions'):
                temp_model = main_models.CroppingSuggestion()
                self.cropping_suggestions.append(temp_model.from_map(k1))

        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')

        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ETag') is not None:
            self.etag = m.get('ETag')

        if m.get('EXIF') is not None:
            self.exif = m.get('EXIF')

        self.elements = []
        if m.get('Elements') is not None:
            for k1 in m.get('Elements'):
                temp_model = main_models.Element()
                self.elements.append(temp_model.from_map(k1))

        if m.get('FigureCount') is not None:
            self.figure_count = m.get('FigureCount')

        self.figures = []
        if m.get('Figures') is not None:
            for k1 in m.get('Figures'):
                temp_model = main_models.Figure()
                self.figures.append(temp_model.from_map(k1))

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
            temp_model = main_models.ImageScore()
            self.image_score = temp_model.from_map(m.get('ImageScore'))

        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')

        if m.get('Insights') is not None:
            temp_model = main_models.Insights()
            self.insights = temp_model.from_map(m.get('Insights'))

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('LatLong') is not None:
            self.lat_long = m.get('LatLong')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        self.ocrcontents = []
        if m.get('OCRContents') is not None:
            for k1 in m.get('OCRContents'):
                temp_model = main_models.OCRContents()
                self.ocrcontents.append(temp_model.from_map(k1))

        if m.get('OCRTexts') is not None:
            self.ocrtexts = m.get('OCRTexts')

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

        if m.get('ObjectStatus') is not None:
            self.object_status = m.get('ObjectStatus')

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

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        self.scene_elements = []
        if m.get('SceneElements') is not None:
            for k1 in m.get('SceneElements'):
                temp_model = main_models.SceneElement()
                self.scene_elements.append(temp_model.from_map(k1))

        if m.get('SemanticTypes') is not None:
            self.semantic_types = m.get('SemanticTypes')

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
            for k1 in m.get('Subtitles'):
                temp_model = main_models.SubtitleStream()
                self.subtitles.append(temp_model.from_map(k1))

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
            for k1 in m.get('VideoStreams'):
                temp_model = main_models.VideoStream()
                self.video_streams.append(temp_model.from_map(k1))

        if m.get('VideoWidth') is not None:
            self.video_width = m.get('VideoWidth')

        return self

