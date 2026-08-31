class DuplexTelephonyVoiceAgentTurnOrchestratorClient:
    def orchestrate_telephony_call(self, recipient_phone_e164='+14155552671', campaign_objective='HEALTHCARE_APPOINTMENT_RESCHEDULING', max_turns=8):
        return {
            'call_session_id': 'tel_orn_5519',
            'call_duration_seconds': 142,
            'turns_exchanged_count': 6,
            'speech_interruption_latency_ms': 180,
            'intent_resolution_status': 'APPOINTMENT_CONFIRMED_SLOT_SECURED',
            'call_recording_wav_url': 'https://telephony.genpark.ai/recordings/5519.wav',
            'call_transcript_json_url': 'https://telephony.genpark.ai/transcripts/5519.json'
        }
