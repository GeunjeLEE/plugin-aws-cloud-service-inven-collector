# from schematics.types import ModelType, StringType, PolyModelType
#
# from spaceone.inventory.connector.aws_kinesis_data_streams_connector.schema.data import StreamDescription
# from spaceone.inventory.libs.schema.dynamic_field import TextDyField, ListDyField, EnumDyField
# from spaceone.inventory.libs.schema.dynamic_layout import ItemDynamicLayout, TableDynamicLayout, ListDynamicLayout
# from spaceone.inventory.libs.schema.resource import CloudServiceResource, CloudServiceResponse, CloudServiceMeta
#
# '''
# KinesisDataStreams
# '''
# # TAB - Detail
# kds_meta_detail = ItemDynamicLayout.set_fields('Details', fields=[
#     TextDyField.data_source('Status', 'data.stream_status_display'),
#     TextDyField.data_source('ARN', 'data.stream_arn'),
#     TextDyField.data_source('Data retention period', 'data.stream_creation_timestamp')
# ])
#
# # TAB - Configuration
# kds_meta_stream_capacity = ItemDynamicLayout.set_fields('Stream capacity', fields=[
#     TextDyField.data_source('Number of open shards', 'data.open_shards_num')
# ])
#
# kds_meta_tags = TableDynamicLayout.set_fields('Tags', 'data.tags', fields=[
#     TextDyField.data_source('Key', 'key'),
#     TextDyField.data_source('Value', 'value'),
# ])
#
# kds_meta_encryption = ItemDynamicLayout.set_fields('Encryption', fields=[
#     TextDyField.data_source('Server-side encryption', 'data.encryption_display')
# ])
#
# kds_data_retention = ItemDynamicLayout.set_fields('Data retention', fields=[
#     TextDyField.data_source('Data retention period', 'data.retention_period_display_details')
# ])
#
# kds_enhanced_metrics = ItemDynamicLayout.set_fields('Enhanced (shard-level) metrics', fields=[
#     ListDyField.data_source('Enhanced (shard-level) metrics', 'data.shard_level_metrics', options={
#         'delimiter': '<br>'
#     })
# ])
#
# kds_meta_configuration = ListDynamicLayout.set_layouts('Configuration',
#                                                        layouts=[kds_meta_stream_capacity, kds_meta_tags,
#                                                                 kds_meta_encryption, kds_data_retention,
#                                                                 kds_enhanced_metrics])
# # TAB - Enhanced fan-out
# kds_meta_consumers_using_enhanced_fan_out = \
#     TableDynamicLayout.set_fields('Consumers using enhanced fan-out', 'data.consumers',
#                                   fields=[
#                                       TextDyField.data_source('Consumer name', 'consumer_name'),
#                                       EnumDyField.data_source('Registration status', 'data.consumer_status',
#                                                               default_state={'safe': ['Active'],
#                                                                              'warning': ['Creating', 'Deleting']}),
#                                       EnumDyField.data_source('Registration date', 'data.consumer_creation_timestamp')
#                                   ])
# kds_meta_enhanced_fan_out = ListDynamicLayout.set_layouts('Enhanced fan-out',
#                                                           layouts=[kds_meta_consumers_using_enhanced_fan_out])
# # Overall
# kds_meta = CloudServiceMeta.set_layouts([kds_meta_detail, kds_meta_configuration, kds_meta_enhanced_fan_out])
#
#
# class KDSResource(CloudServiceResource):
#     cloud_service_group = StringType(default='KinesisDataStreamsManager')
#
#
# class StreamResource(KDSResource):
#     cloud_service_type = StringType(default='StreamDescription')
#     data = ModelType(StreamDescription)
#     _metadata = ModelType(CloudServiceMeta, default=kds_meta, serialized_name='metadata')
#
#
# class KDSResponse(CloudServiceResponse):
#     resource = PolyModelType(StreamResource)
