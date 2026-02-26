# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class InputFile(DaraModel):
    def __init__(
        self,
        addresses: List[main_models.Address] = None,
        album: str = None,
        album_artist: str = None,
        artist: str = None,
        composer: str = None,
        content_type: str = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        figures: List[main_models.InputFileFigures] = None,
        file_hash: str = None,
        labels: List[main_models.Label] = None,
        lat_long: str = None,
        media_type: str = None,
        ossuri: str = None,
        performer: str = None,
        produce_time: str = None,
        title: str = None,
        uri: str = None,
    ):
        # The addresses.
        self.addresses = addresses
        # The album.
        self.album = album
        # The album artist.
        self.album_artist = album_artist
        # The artist.
        self.artist = artist
        # The composer.
        self.composer = composer
        # In most cases, you can leave this parameter empty. The Multipurpose Internet Mail Extensions (MIME) type of the file.
        self.content_type = content_type
        # The custom ID of the file. This parameter is optional. When the metadata of the file is indexed into the dataset, the custom ID is stored as the data attribute. You can map the custom ID to other data in your business system. You can configure this parameter based on your business requirements. For example, you can associate a URI with an ID in your business system. We recommend that you set this parameter to a unique value.
        # 
        # This parameter supports prefix searches and sorting during queries. For more information, see [Supported fields and operators](https://help.aliyun.com/document_detail/252856.html).
        self.custom_id = custom_id
        # The custom labels of the file. This parameter is optional. The parameter stores custom key-value labels, which can be used to filter data. For more information, see [Supported fields and operators](https://help.aliyun.com/document_detail/252856.html).
        self.custom_labels = custom_labels
        # This parameter is optional. The persons. This parameter is used to remove a face from a face group or modify a face group. For more information, see [Face clustering](https://help.aliyun.com/document_detail/477175.html).
        # 
        # >  This parameter takes effect only for the UpdateFileMeta or BatchUpdateFileMeta operation.
        self.figures = figures
        # The file hash. In most cases, you can leave this parameter empty. This parameter is required only when the URI parameter specifies a file in Photo and Drive Service.
        self.file_hash = file_hash
        # The intelligent labels.
        self.labels = labels
        # The GPS latitude and longitude information.
        self.lat_long = lat_long
        # In most cases, you can leave this parameter empty. The media type of the file.
        # 
        # Enumerated values:
        # 
        # *   image
        # *   other
        # *   document
        # *   archive
        # *   video
        # *   audio
        self.media_type = media_type
        # The path of the OSS object. In most cases, you can leave this parameter empty. You can specify this parameter only if the URI parameter specifies a file in Photo and Drive Service.
        self.ossuri = ossuri
        # The performer.
        self.performer = performer
        # The time when the image was taken.
        self.produce_time = produce_time
        # The file title.
        self.title = title
        # The URI of the file for which you want to create or update an index in the request. This parameter is required. The URI can represent an object in Object Storage Service (OSS) or a file in Photo and Drive Service.
        # 
        # The OSS URI must be in the oss://${Bucket}/${Object} format. `${Bucket}` specifies the name of the OSS bucket that is in the same region as the current project. `${Object}` specifies the full file path that contains the object name extension.
        # 
        # The URI of a file in Photo and Drive Service must be in the `pds://domains/${domain}/drives/${drive}/files/${file}/revisions/${revision}` format.
        # 
        # >  URIs that start with HTTP are not supported.
        self.uri = uri

    def validate(self):
        if self.addresses:
            for v1 in self.addresses:
                 if v1:
                    v1.validate()
        if self.figures:
            for v1 in self.figures:
                 if v1:
                    v1.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.composer is not None:
            result['Composer'] = self.composer

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.custom_id is not None:
            result['CustomId'] = self.custom_id

        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels

        result['Figures'] = []
        if self.figures is not None:
            for k1 in self.figures:
                result['Figures'].append(k1.to_map() if k1 else None)

        if self.file_hash is not None:
            result['FileHash'] = self.file_hash

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.lat_long is not None:
            result['LatLong'] = self.lat_long

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.ossuri is not None:
            result['OSSURI'] = self.ossuri

        if self.performer is not None:
            result['Performer'] = self.performer

        if self.produce_time is not None:
            result['ProduceTime'] = self.produce_time

        if self.title is not None:
            result['Title'] = self.title

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('Composer') is not None:
            self.composer = m.get('Composer')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')

        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')

        self.figures = []
        if m.get('Figures') is not None:
            for k1 in m.get('Figures'):
                temp_model = main_models.InputFileFigures()
                self.figures.append(temp_model.from_map(k1))

        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

        if m.get('LatLong') is not None:
            self.lat_long = m.get('LatLong')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('OSSURI') is not None:
            self.ossuri = m.get('OSSURI')

        if m.get('Performer') is not None:
            self.performer = m.get('Performer')

        if m.get('ProduceTime') is not None:
            self.produce_time = m.get('ProduceTime')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

class InputFileFigures(DaraModel):
    def __init__(
        self,
        figure_cluster_id: str = None,
        figure_id: str = None,
        figure_type: str = None,
    ):
        # The ID of the face cluster. The following IDs of special face clusters are reserved:
        # 
        # *   figure-cluster-id-independent: indicates that the face does not belong to any face cluster. The face may be added to a face cluster in subsequent face clustering tasks after new images are added to the dataset.
        # *   figure-cluster-id-unavailable: indicates that the face has not been included in a face clustering task since a new image was added to the dataset.
        self.figure_cluster_id = figure_cluster_id
        # The person ID.
        self.figure_id = figure_id
        # The figure type. Set this parameter to `face`.
        self.figure_type = figure_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

