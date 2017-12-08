"""Generated message classes for videointelligence version v1beta1.

Google Cloud Video Intelligence API.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'videointelligence'


class GoogleCloudVideointelligenceV1AnnotateVideoProgress(_messages.Message):
  """Video annotation progress. Included in the `metadata` field of the
  `Operation` returned by the `GetOperation` call of the
  `google::longrunning::Operations` service.

  Fields:
    annotationProgress: Progress metadata for all videos specified in
      `AnnotateVideoRequest`.
  """

  annotationProgress = _messages.MessageField('GoogleCloudVideointelligenceV1VideoAnnotationProgress', 1, repeated=True)


class GoogleCloudVideointelligenceV1AnnotateVideoResponse(_messages.Message):
  """Video annotation response. Included in the `response` field of the
  `Operation` returned by the `GetOperation` call of the
  `google::longrunning::Operations` service.

  Fields:
    annotationResults: Annotation results for all videos specified in
      `AnnotateVideoRequest`.
  """

  annotationResults = _messages.MessageField('GoogleCloudVideointelligenceV1VideoAnnotationResults', 1, repeated=True)


class GoogleCloudVideointelligenceV1LabelAnnotation(_messages.Message):
  """Label annotation.

  Fields:
    description: Textual description, e.g. `Fixed-gear bicycle`.
    languageCode: Language code for `description` in BCP-47 format.
    locations: Where the label was detected and with what confidence.
  """

  description = _messages.StringField(1)
  languageCode = _messages.StringField(2)
  locations = _messages.MessageField('GoogleCloudVideointelligenceV1LabelLocation', 3, repeated=True)


class GoogleCloudVideointelligenceV1LabelLocation(_messages.Message):
  """Label location.

  Enums:
    LevelValueValuesEnum: Label level.

  Fields:
    confidence: Confidence that the label is accurate. Range: [0, 1].
    level: Label level.
    segment: Video segment. Unset for video-level labels. Set to a frame
      timestamp for frame-level labels. Otherwise, corresponds to one of
      `AnnotateSpec.segments` (if specified) or to shot boundaries (if
      requested).
  """

  class LevelValueValuesEnum(_messages.Enum):
    """Label level.

    Values:
      LABEL_LEVEL_UNSPECIFIED: Unspecified.
      VIDEO_LEVEL: Video-level. Corresponds to the whole video.
      SEGMENT_LEVEL: Segment-level. Corresponds to one of
        `AnnotateSpec.segments`.
      SHOT_LEVEL: Shot-level. Corresponds to a single shot (i.e. a series of
        frames without a major camera position or background change).
      FRAME_LEVEL: Frame-level. Corresponds to a single video frame.
    """
    LABEL_LEVEL_UNSPECIFIED = 0
    VIDEO_LEVEL = 1
    SEGMENT_LEVEL = 2
    SHOT_LEVEL = 3
    FRAME_LEVEL = 4

  confidence = _messages.FloatField(1, variant=_messages.Variant.FLOAT)
  level = _messages.EnumField('LevelValueValuesEnum', 2)
  segment = _messages.MessageField('GoogleCloudVideointelligenceV1VideoSegment', 3)


class GoogleCloudVideointelligenceV1SafeSearchAnnotation(_messages.Message):
  """Safe search annotation (based on per-frame visual signals only). If no
  unsafe content has been detected in a frame, no annotations are present for
  that frame.

  Enums:
    AdultValueValuesEnum: Likelihood of adult content.

  Fields:
    adult: Likelihood of adult content.
    time: Time-offset, relative to the beginning of the video, corresponding
      to the video frame for this annotation.
  """

  class AdultValueValuesEnum(_messages.Enum):
    """Likelihood of adult content.

    Values:
      UNKNOWN: Unknown likelihood.
      VERY_UNLIKELY: Very unlikely.
      UNLIKELY: Unlikely.
      POSSIBLE: Possible.
      LIKELY: Likely.
      VERY_LIKELY: Very likely.
    """
    UNKNOWN = 0
    VERY_UNLIKELY = 1
    UNLIKELY = 2
    POSSIBLE = 3
    LIKELY = 4
    VERY_LIKELY = 5

  adult = _messages.EnumField('AdultValueValuesEnum', 1)
  time = _messages.StringField(2)


class GoogleCloudVideointelligenceV1VideoAnnotationProgress(_messages.Message):
  """Annotation progress for a single video.

  Fields:
    inputUri: Video file location in [Google Cloud
      Storage](https://cloud.google.com/storage/).
    progressPercent: Approximate percentage processed thus far. Guaranteed to
      be 100 when fully processed.
    startTime: Time when the request was received.
    updateTime: Time of the most recent update.
  """

  inputUri = _messages.StringField(1)
  progressPercent = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  startTime = _messages.StringField(3)
  updateTime = _messages.StringField(4)


class GoogleCloudVideointelligenceV1VideoAnnotationResults(_messages.Message):
  """Annotation results for a single video.

  Fields:
    error: If set, indicates an error. Note that for a single
      `AnnotateVideoRequest` some videos may succeed and some may fail.
    inputUri: Video file location in [Google Cloud
      Storage](https://cloud.google.com/storage/).
    labelAnnotations: Label annotations. There is exactly one element for each
      unique label.
    safeSearchAnnotations: Safe search annotations.
    shotAnnotations: Shot annotations. Each shot is represented as a video
      segment.
  """

  error = _messages.MessageField('GoogleRpcStatus', 1)
  inputUri = _messages.StringField(2)
  labelAnnotations = _messages.MessageField('GoogleCloudVideointelligenceV1LabelAnnotation', 3, repeated=True)
  safeSearchAnnotations = _messages.MessageField('GoogleCloudVideointelligenceV1SafeSearchAnnotation', 4, repeated=True)
  shotAnnotations = _messages.MessageField('GoogleCloudVideointelligenceV1VideoSegment', 5, repeated=True)


class GoogleCloudVideointelligenceV1VideoSegment(_messages.Message):
  """Video segment.

  Fields:
    endTime: Time-offset, relative to the beginning of the video,
      corresponding to the end of the segment (inclusive).
    startTime: Time-offset, relative to the beginning of the video,
      corresponding to the start of the segment (inclusive).
  """

  endTime = _messages.StringField(1)
  startTime = _messages.StringField(2)


class GoogleCloudVideointelligenceV1beta1AnnotateVideoProgress(_messages.Message):
  """Video annotation progress. Included in the `metadata` field of the
  `Operation` returned by the `GetOperation` call of the
  `google::longrunning::Operations` service.

  Fields:
    annotationProgress: Progress metadata for all videos specified in
      `AnnotateVideoRequest`.
  """

  annotationProgress = _messages.MessageField('GoogleCloudVideointelligenceV1beta1VideoAnnotationProgress', 1, repeated=True)


class GoogleCloudVideointelligenceV1beta1AnnotateVideoRequest(_messages.Message):
  """Video annotation request.

  Enums:
    FeaturesValueListEntryValuesEnum:

  Fields:
    features: Requested video annotation features.
    inputContent: The video data bytes. Encoding: base64. If unset, the input
      video(s) should be specified via `input_uri`. If set, `input_uri` should
      be unset.
    inputUri: Input video location. Currently, only [Google Cloud
      Storage](https://cloud.google.com/storage/) URIs are supported, which
      must be specified in the following format: `gs://bucket-id/object-id`
      (other URI formats return google.rpc.Code.INVALID_ARGUMENT). For more
      information, see [Request URIs](/storage/docs/reference-uris). A video
      URI may include wildcards in `object-id`, and thus identify multiple
      videos. Supported wildcards: '*' to match 0 or more characters; '?' to
      match 1 character. If unset, the input video should be embedded in the
      request as `input_content`. If set, `input_content` should be unset.
    locationId: Optional cloud region where annotation should take place.
      Supported cloud regions: `us-east1`, `us-west1`, `europe-west1`, `asia-
      east1`. If no region is specified, a region will be determined based on
      video file location.
    outputUri: Optional location where the output (in JSON format) should be
      stored. Currently, only [Google Cloud
      Storage](https://cloud.google.com/storage/) URIs are supported, which
      must be specified in the following format: `gs://bucket-id/object-id`
      (other URI formats return google.rpc.Code.INVALID_ARGUMENT). For more
      information, see [Request URIs](/storage/docs/reference-uris).
    videoContext: Additional video context and/or feature-specific parameters.
  """

  class FeaturesValueListEntryValuesEnum(_messages.Enum):
    """FeaturesValueListEntryValuesEnum enum type.

    Values:
      FEATURE_UNSPECIFIED: <no description>
      LABEL_DETECTION: <no description>
      SHOT_CHANGE_DETECTION: <no description>
      SAFE_SEARCH_DETECTION: <no description>
    """
    FEATURE_UNSPECIFIED = 0
    LABEL_DETECTION = 1
    SHOT_CHANGE_DETECTION = 2
    SAFE_SEARCH_DETECTION = 3

  features = _messages.EnumField('FeaturesValueListEntryValuesEnum', 1, repeated=True)
  inputContent = _messages.StringField(2)
  inputUri = _messages.StringField(3)
  locationId = _messages.StringField(4)
  outputUri = _messages.StringField(5)
  videoContext = _messages.MessageField('GoogleCloudVideointelligenceV1beta1VideoContext', 6)


class GoogleCloudVideointelligenceV1beta1AnnotateVideoResponse(_messages.Message):
  """Video annotation response. Included in the `response` field of the
  `Operation` returned by the `GetOperation` call of the
  `google::longrunning::Operations` service.

  Fields:
    annotationResults: Annotation results for all videos specified in
      `AnnotateVideoRequest`.
  """

  annotationResults = _messages.MessageField('GoogleCloudVideointelligenceV1beta1VideoAnnotationResults', 1, repeated=True)


class GoogleCloudVideointelligenceV1beta1LabelAnnotation(_messages.Message):
  """Label annotation.

  Fields:
    description: Textual description, e.g. `Fixed-gear bicycle`.
    languageCode: Language code for `description` in BCP-47 format.
    locations: Where the label was detected and with what confidence.
  """

  description = _messages.StringField(1)
  languageCode = _messages.StringField(2)
  locations = _messages.MessageField('GoogleCloudVideointelligenceV1beta1LabelLocation', 3, repeated=True)


class GoogleCloudVideointelligenceV1beta1LabelLocation(_messages.Message):
  """Label location.

  Enums:
    LevelValueValuesEnum: Label level.

  Fields:
    confidence: Confidence that the label is accurate. Range: [0, 1].
    level: Label level.
    segment: Video segment. Set to [-1, -1] for video-level labels. Set to
      [timestamp, timestamp] for frame-level labels. Otherwise, corresponds to
      one of `AnnotateSpec.segments` (if specified) or to shot boundaries (if
      requested).
  """

  class LevelValueValuesEnum(_messages.Enum):
    """Label level.

    Values:
      LABEL_LEVEL_UNSPECIFIED: Unspecified.
      VIDEO_LEVEL: Video-level. Corresponds to the whole video.
      SEGMENT_LEVEL: Segment-level. Corresponds to one of
        `AnnotateSpec.segments`.
      SHOT_LEVEL: Shot-level. Corresponds to a single shot (i.e. a series of
        frames without a major camera position or background change).
      FRAME_LEVEL: Frame-level. Corresponds to a single video frame.
    """
    LABEL_LEVEL_UNSPECIFIED = 0
    VIDEO_LEVEL = 1
    SEGMENT_LEVEL = 2
    SHOT_LEVEL = 3
    FRAME_LEVEL = 4

  confidence = _messages.FloatField(1, variant=_messages.Variant.FLOAT)
  level = _messages.EnumField('LevelValueValuesEnum', 2)
  segment = _messages.MessageField('GoogleCloudVideointelligenceV1beta1VideoSegment', 3)


class GoogleCloudVideointelligenceV1beta1SafeSearchAnnotation(_messages.Message):
  """Safe search annotation (based on per-frame visual signals only). If no
  unsafe content has been detected in a frame, no annotations are present for
  that frame. If only some types of unsafe content have been detected in a
  frame, the likelihood is set to `UNKNOWN` for all other types of unsafe
  content.

  Enums:
    AdultValueValuesEnum: Likelihood of adult content.
    MedicalValueValuesEnum: Likelihood of medical content.
    RacyValueValuesEnum: Likelihood of racy content.
    SpoofValueValuesEnum: Likelihood that an obvious modification was made to
      the original version to make it appear funny or offensive.
    ViolentValueValuesEnum: Likelihood of violent content.

  Fields:
    adult: Likelihood of adult content.
    medical: Likelihood of medical content.
    racy: Likelihood of racy content.
    spoof: Likelihood that an obvious modification was made to the original
      version to make it appear funny or offensive.
    timeOffset: Video time offset in microseconds.
    violent: Likelihood of violent content.
  """

  class AdultValueValuesEnum(_messages.Enum):
    """Likelihood of adult content.

    Values:
      UNKNOWN: Unknown likelihood.
      VERY_UNLIKELY: Very unlikely.
      UNLIKELY: Unlikely.
      POSSIBLE: Possible.
      LIKELY: Likely.
      VERY_LIKELY: Very likely.
    """
    UNKNOWN = 0
    VERY_UNLIKELY = 1
    UNLIKELY = 2
    POSSIBLE = 3
    LIKELY = 4
    VERY_LIKELY = 5

  class MedicalValueValuesEnum(_messages.Enum):
    """Likelihood of medical content.

    Values:
      UNKNOWN: Unknown likelihood.
      VERY_UNLIKELY: Very unlikely.
      UNLIKELY: Unlikely.
      POSSIBLE: Possible.
      LIKELY: Likely.
      VERY_LIKELY: Very likely.
    """
    UNKNOWN = 0
    VERY_UNLIKELY = 1
    UNLIKELY = 2
    POSSIBLE = 3
    LIKELY = 4
    VERY_LIKELY = 5

  class RacyValueValuesEnum(_messages.Enum):
    """Likelihood of racy content.

    Values:
      UNKNOWN: Unknown likelihood.
      VERY_UNLIKELY: Very unlikely.
      UNLIKELY: Unlikely.
      POSSIBLE: Possible.
      LIKELY: Likely.
      VERY_LIKELY: Very likely.
    """
    UNKNOWN = 0
    VERY_UNLIKELY = 1
    UNLIKELY = 2
    POSSIBLE = 3
    LIKELY = 4
    VERY_LIKELY = 5

  class SpoofValueValuesEnum(_messages.Enum):
    """Likelihood that an obvious modification was made to the original
    version to make it appear funny or offensive.

    Values:
      UNKNOWN: Unknown likelihood.
      VERY_UNLIKELY: Very unlikely.
      UNLIKELY: Unlikely.
      POSSIBLE: Possible.
      LIKELY: Likely.
      VERY_LIKELY: Very likely.
    """
    UNKNOWN = 0
    VERY_UNLIKELY = 1
    UNLIKELY = 2
    POSSIBLE = 3
    LIKELY = 4
    VERY_LIKELY = 5

  class ViolentValueValuesEnum(_messages.Enum):
    """Likelihood of violent content.

    Values:
      UNKNOWN: Unknown likelihood.
      VERY_UNLIKELY: Very unlikely.
      UNLIKELY: Unlikely.
      POSSIBLE: Possible.
      LIKELY: Likely.
      VERY_LIKELY: Very likely.
    """
    UNKNOWN = 0
    VERY_UNLIKELY = 1
    UNLIKELY = 2
    POSSIBLE = 3
    LIKELY = 4
    VERY_LIKELY = 5

  adult = _messages.EnumField('AdultValueValuesEnum', 1)
  medical = _messages.EnumField('MedicalValueValuesEnum', 2)
  racy = _messages.EnumField('RacyValueValuesEnum', 3)
  spoof = _messages.EnumField('SpoofValueValuesEnum', 4)
  timeOffset = _messages.IntegerField(5)
  violent = _messages.EnumField('ViolentValueValuesEnum', 6)


class GoogleCloudVideointelligenceV1beta1VideoAnnotationProgress(_messages.Message):
  """Annotation progress for a single video.

  Fields:
    inputUri: Video file location in [Google Cloud
      Storage](https://cloud.google.com/storage/).
    progressPercent: Approximate percentage processed thus far. Guaranteed to
      be 100 when fully processed.
    startTime: Time when the request was received.
    updateTime: Time of the most recent update.
  """

  inputUri = _messages.StringField(1)
  progressPercent = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  startTime = _messages.StringField(3)
  updateTime = _messages.StringField(4)


class GoogleCloudVideointelligenceV1beta1VideoAnnotationResults(_messages.Message):
  """Annotation results for a single video.

  Fields:
    error: If set, indicates an error. Note that for a single
      `AnnotateVideoRequest` some videos may succeed and some may fail.
    inputUri: Video file location in [Google Cloud
      Storage](https://cloud.google.com/storage/).
    labelAnnotations: Label annotations. There is exactly one element for each
      unique label.
    safeSearchAnnotations: Safe search annotations.
    shotAnnotations: Shot annotations. Each shot is represented as a video
      segment.
  """

  error = _messages.MessageField('GoogleRpcStatus', 1)
  inputUri = _messages.StringField(2)
  labelAnnotations = _messages.MessageField('GoogleCloudVideointelligenceV1beta1LabelAnnotation', 3, repeated=True)
  safeSearchAnnotations = _messages.MessageField('GoogleCloudVideointelligenceV1beta1SafeSearchAnnotation', 4, repeated=True)
  shotAnnotations = _messages.MessageField('GoogleCloudVideointelligenceV1beta1VideoSegment', 5, repeated=True)


class GoogleCloudVideointelligenceV1beta1VideoContext(_messages.Message):
  """Video context and/or feature-specific parameters.

  Enums:
    LabelDetectionModeValueValuesEnum: If label detection has been requested,
      what labels should be detected in addition to video-level labels or
      segment-level labels. If unspecified, defaults to `SHOT_MODE`.

  Fields:
    labelDetectionMode: If label detection has been requested, what labels
      should be detected in addition to video-level labels or segment-level
      labels. If unspecified, defaults to `SHOT_MODE`.
    labelDetectionModel: Model to use for label detection. Supported values:
      "latest" and "stable" (the default).
    safeSearchDetectionModel: Model to use for safe search detection.
      Supported values: "latest" and "stable" (the default).
    segments: Video segments to annotate. The segments may overlap and are not
      required to be contiguous or span the whole video. If unspecified, each
      video is treated as a single segment.
    shotChangeDetectionModel: Model to use for shot change detection.
      Supported values: "latest" and "stable" (the default).
    stationaryCamera: Whether the video has been shot from a stationary (i.e.
      non-moving) camera. When set to true, might improve detection accuracy
      for moving objects.
  """

  class LabelDetectionModeValueValuesEnum(_messages.Enum):
    """If label detection has been requested, what labels should be detected
    in addition to video-level labels or segment-level labels. If unspecified,
    defaults to `SHOT_MODE`.

    Values:
      LABEL_DETECTION_MODE_UNSPECIFIED: Unspecified.
      SHOT_MODE: Detect shot-level labels.
      FRAME_MODE: Detect frame-level labels.
      SHOT_AND_FRAME_MODE: Detect both shot-level and frame-level labels.
    """
    LABEL_DETECTION_MODE_UNSPECIFIED = 0
    SHOT_MODE = 1
    FRAME_MODE = 2
    SHOT_AND_FRAME_MODE = 3

  labelDetectionMode = _messages.EnumField('LabelDetectionModeValueValuesEnum', 1)
  labelDetectionModel = _messages.StringField(2)
  safeSearchDetectionModel = _messages.StringField(3)
  segments = _messages.MessageField('GoogleCloudVideointelligenceV1beta1VideoSegment', 4, repeated=True)
  shotChangeDetectionModel = _messages.StringField(5)
  stationaryCamera = _messages.BooleanField(6)


class GoogleCloudVideointelligenceV1beta1VideoSegment(_messages.Message):
  """Video segment.

  Fields:
    endTimeOffset: End offset in microseconds (inclusive). Unset means 0.
    startTimeOffset: Start offset in microseconds (inclusive). Unset means 0.
  """

  endTimeOffset = _messages.IntegerField(1)
  startTimeOffset = _messages.IntegerField(2)


class GoogleCloudVideointelligenceV1beta2AnnotateVideoProgress(_messages.Message):
  """Video annotation progress. Included in the `metadata` field of the
  `Operation` returned by the `GetOperation` call of the
  `google::longrunning::Operations` service.

  Fields:
    annotationProgress: Progress metadata for all videos specified in
      `AnnotateVideoRequest`.
  """

  annotationProgress = _messages.MessageField('GoogleCloudVideointelligenceV1beta2VideoAnnotationProgress', 1, repeated=True)


class GoogleCloudVideointelligenceV1beta2AnnotateVideoResponse(_messages.Message):
  """Video annotation response. Included in the `response` field of the
  `Operation` returned by the `GetOperation` call of the
  `google::longrunning::Operations` service.

  Fields:
    annotationResults: Annotation results for all videos specified in
      `AnnotateVideoRequest`.
  """

  annotationResults = _messages.MessageField('GoogleCloudVideointelligenceV1beta2VideoAnnotationResults', 1, repeated=True)


class GoogleCloudVideointelligenceV1beta2Entity(_messages.Message):
  """Detected entity from video analysis.

  Fields:
    description: Textual description, e.g. `Fixed-gear bicycle`.
    entityId: Opaque entity ID. Some IDs may be available in [Google Knowledge
      Graph Search API](https://developers.google.com/knowledge-graph/).
    languageCode: Language code for `description` in BCP-47 format.
  """

  description = _messages.StringField(1)
  entityId = _messages.StringField(2)
  languageCode = _messages.StringField(3)


class GoogleCloudVideointelligenceV1beta2ExplicitContentAnnotation(_messages.Message):
  """Explicit content annotation (based on per-frame visual signals only). If
  no explicit content has been detected in a frame, no annotations are present
  for that frame.

  Fields:
    frames: All video frames where explicit content was detected.
  """

  frames = _messages.MessageField('GoogleCloudVideointelligenceV1beta2ExplicitContentFrame', 1, repeated=True)


class GoogleCloudVideointelligenceV1beta2ExplicitContentFrame(_messages.Message):
  """Video frame level annotation results for explicit content.

  Enums:
    PornographyLikelihoodValueValuesEnum: Likelihood of the pornography
      content..

  Fields:
    pornographyLikelihood: Likelihood of the pornography content..
    timeOffset: Time-offset, relative to the beginning of the video,
      corresponding to the video frame for this location.
  """

  class PornographyLikelihoodValueValuesEnum(_messages.Enum):
    """Likelihood of the pornography content..

    Values:
      LIKELIHOOD_UNSPECIFIED: Unspecified likelihood.
      VERY_UNLIKELY: Very unlikely.
      UNLIKELY: Unlikely.
      POSSIBLE: Possible.
      LIKELY: Likely.
      VERY_LIKELY: Very likely.
    """
    LIKELIHOOD_UNSPECIFIED = 0
    VERY_UNLIKELY = 1
    UNLIKELY = 2
    POSSIBLE = 3
    LIKELY = 4
    VERY_LIKELY = 5

  pornographyLikelihood = _messages.EnumField('PornographyLikelihoodValueValuesEnum', 1)
  timeOffset = _messages.StringField(2)


class GoogleCloudVideointelligenceV1beta2LabelAnnotation(_messages.Message):
  """Label annotation.

  Fields:
    categoryEntities: Common categories for the detected entity. E.g. when the
      label is `Terrier` the category is likely `dog`. And in some cases there
      might be more than one categories e.g. `Terrier` could also be a `pet`.
    entity: Detected entity.
    frames: All video frames where a label was detected.
    segments: All video segments where a label was detected.
  """

  categoryEntities = _messages.MessageField('GoogleCloudVideointelligenceV1beta2Entity', 1, repeated=True)
  entity = _messages.MessageField('GoogleCloudVideointelligenceV1beta2Entity', 2)
  frames = _messages.MessageField('GoogleCloudVideointelligenceV1beta2LabelFrame', 3, repeated=True)
  segments = _messages.MessageField('GoogleCloudVideointelligenceV1beta2LabelSegment', 4, repeated=True)


class GoogleCloudVideointelligenceV1beta2LabelFrame(_messages.Message):
  """Video frame level annotation results for label detection.

  Fields:
    confidence: Confidence that the label is accurate. Range: [0, 1].
    timeOffset: Time-offset, relative to the beginning of the video,
      corresponding to the video frame for this location.
  """

  confidence = _messages.FloatField(1, variant=_messages.Variant.FLOAT)
  timeOffset = _messages.StringField(2)


class GoogleCloudVideointelligenceV1beta2LabelSegment(_messages.Message):
  """Video segment level annotation results for label detection.

  Fields:
    confidence: Confidence that the label is accurate. Range: [0, 1].
    segment: Video segment where a label was detected.
  """

  confidence = _messages.FloatField(1, variant=_messages.Variant.FLOAT)
  segment = _messages.MessageField('GoogleCloudVideointelligenceV1beta2VideoSegment', 2)


class GoogleCloudVideointelligenceV1beta2VideoAnnotationProgress(_messages.Message):
  """Annotation progress for a single video.

  Fields:
    inputUri: Video file location in [Google Cloud
      Storage](https://cloud.google.com/storage/).
    progressPercent: Approximate percentage processed thus far. Guaranteed to
      be 100 when fully processed.
    startTime: Time when the request was received.
    updateTime: Time of the most recent update.
  """

  inputUri = _messages.StringField(1)
  progressPercent = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  startTime = _messages.StringField(3)
  updateTime = _messages.StringField(4)


class GoogleCloudVideointelligenceV1beta2VideoAnnotationResults(_messages.Message):
  """Annotation results for a single video.

  Fields:
    error: If set, indicates an error. Note that for a single
      `AnnotateVideoRequest` some videos may succeed and some may fail.
    explicitAnnotation: Explicit content annotation.
    frameLabelAnnotations: Label annotations on frame level. There is exactly
      one element for each unique label.
    inputUri: Video file location in [Google Cloud
      Storage](https://cloud.google.com/storage/).
    segmentLabelAnnotations: Label annotations on video level or user
      specified segment level. There is exactly one element for each unique
      label.
    shotAnnotations: Shot annotations. Each shot is represented as a video
      segment.
    shotLabelAnnotations: Label annotations on shot level. There is exactly
      one element for each unique label.
  """

  error = _messages.MessageField('GoogleRpcStatus', 1)
  explicitAnnotation = _messages.MessageField('GoogleCloudVideointelligenceV1beta2ExplicitContentAnnotation', 2)
  frameLabelAnnotations = _messages.MessageField('GoogleCloudVideointelligenceV1beta2LabelAnnotation', 3, repeated=True)
  inputUri = _messages.StringField(4)
  segmentLabelAnnotations = _messages.MessageField('GoogleCloudVideointelligenceV1beta2LabelAnnotation', 5, repeated=True)
  shotAnnotations = _messages.MessageField('GoogleCloudVideointelligenceV1beta2VideoSegment', 6, repeated=True)
  shotLabelAnnotations = _messages.MessageField('GoogleCloudVideointelligenceV1beta2LabelAnnotation', 7, repeated=True)


class GoogleCloudVideointelligenceV1beta2VideoSegment(_messages.Message):
  """Video segment.

  Fields:
    endTimeOffset: Time-offset, relative to the beginning of the video,
      corresponding to the end of the segment (inclusive).
    startTimeOffset: Time-offset, relative to the beginning of the video,
      corresponding to the start of the segment (inclusive).
  """

  endTimeOffset = _messages.StringField(1)
  startTimeOffset = _messages.StringField(2)


class GoogleLongrunningOperation(_messages.Message):
  """This resource represents a long-running operation that is the result of a
  network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation.
      It typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success.
      If the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If true, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation.  It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should have the format of `operations/some/unique/name`.
    response: The normal response of the operation in case of success.  If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    """Service-specific metadata associated with the operation.  It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata.  Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    """The normal response of the operation in case of success.  If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name.  For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('GoogleRpcStatus', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class GoogleRpcStatus(_messages.Message):
  """The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). The error model is designed to be:
  - Simple to use and understand for most users - Flexible enough to meet
  unexpected needs  # Overview  The `Status` message contains three pieces of
  data: error code, error message, and error details. The error code should be
  an enum value of google.rpc.Code, but it may accept additional error codes
  if needed.  The error message should be a developer-facing English message
  that helps developers *understand* and *resolve* the error. If a localized
  user-facing error message is needed, put the localized message in the error
  details or localize it in the client. The optional error details may contain
  arbitrary information about the error. There is a predefined set of error
  detail types in the package `google.rpc` that can be used for common error
  conditions.  # Language mapping  The `Status` message is the logical
  representation of the error model, but it is not necessarily the actual wire
  format. When the `Status` message is exposed in different client libraries
  and different wire protocols, it can be mapped differently. For example, it
  will likely be mapped to some exceptions in Java, but more likely mapped to
  some error codes in C.  # Other uses  The error model and the `Status`
  message can be used in a variety of environments, either with or without
  APIs, to provide a consistent developer experience across different
  environments.  Example uses of this error model include:  - Partial errors.
  If a service needs to return partial errors to the client,     it may embed
  the `Status` in the normal response to indicate the partial     errors.  -
  Workflow errors. A typical workflow has multiple steps. Each step may
  have a `Status` message for error reporting.  - Batch operations. If a
  client uses batch request and batch response, the     `Status` message
  should be used directly inside batch response, one for     each error sub-
  response.  - Asynchronous operations. If an API call embeds asynchronous
  operation     results in its response, the status of those operations should
  be     represented directly using the `Status` message.  - Logging. If some
  API errors are stored in logs, the message `Status` could     be used
  directly after any stripping needed for security/privacy reasons.

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    """A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    bearer_token: OAuth bearer token.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    pp: Pretty-print response.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    """Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    """V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  bearer_token = _messages.StringField(4)
  callback = _messages.StringField(5)
  fields = _messages.StringField(6)
  key = _messages.StringField(7)
  oauth_token = _messages.StringField(8)
  pp = _messages.BooleanField(9, default=True)
  prettyPrint = _messages.BooleanField(10, default=True)
  quotaUser = _messages.StringField(11)
  trace = _messages.StringField(12)
  uploadType = _messages.StringField(13)
  upload_protocol = _messages.StringField(14)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
