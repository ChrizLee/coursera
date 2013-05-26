// Mapper() : Given unique 5-card hand (csv string), return the made hand.
// e.g. 'flush', 'straight', etc 
function Mapper(jsmr_context, dataline) { 
  var cards = dataline.split(',');  // 5 cards like 'QH' (for Q of hearts)
   
  // Get counts of all faces and suits. 
  var counts = { 
      '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, 'T':0, 
      'J':0, 'Q':0, 'K':0, 'A':0, 
      'S':0, 'C':0, 'D':0, 'H':0  // Spades, Clubs, Diamonds, Hearts 
    }; 
  for (var i = 0; i < cards.length; i++) { 
    var card = cards[i]; 
    var face = card[0]; 
    var suit = card[1]; 
    counts[face]++; 
    counts[suit]++; 
  } 
 
  var is_flush = ( 
      (counts['S'] == 5) ||  // 5 Spades ? 
      (counts['C'] == 5) ||  // 5 Clubs ? 
      (counts['D'] == 5) ||  // 5 Diamonds ? 
      (counts['H'] == 5));   // 5 Hearts ? 
 
  var is_straight = false; 
  var straightrunfaces = 'A23456789TJQKA';  // note: ace ('A') appears twice
  for (var i = 0; i < 10; i++) { 
    if (counts[straightrunfaces[i]] &&  
        counts[straightrunfaces[i+1]] && 
        counts[straightrunfaces[i+2]] && 
        counts[straightrunfaces[i+3]] && 
        counts[straightrunfaces[i+4]]) { 
      is_straight = true; 
      break; 
    } 
  } 
  
  var is_4cardstraight = false;
  for (var i = 0; i < 10; i++) { 
    if (counts[straightrunfaces[i]] &&  
        counts[straightrunfaces[i+1]] && 
        counts[straightrunfaces[i+2]] && 
        counts[straightrunfaces[i+3]] && 
        !counts[straightrunfaces[i+4]]) { 
      is_4cardstraight = true; 
      break; 
    } 
  }
 
  var is_quad = false; 
  var is_trip = false; 
  var is_pair = false; 
  var is_two_pair = false; 
  var faces = 'A23456789TJQK'; 
  for (var i = 0; i < faces.length; i++) { 
    switch (counts[faces[i]]) { 
      case 4: is_quad = true; break; 
      case 3: is_trip = true; break; 
      case 2: if (is_pair) { is_two_pair = true; } is_pair = true; break; 
    } 
  } 
 
  // Emit output 
  if (is_straight && is_flush) jsmr_context.Emit('straightflush', '1'); 
  else if (is_4cardstraight) jsmr_context.Emit('4cardstraight', '1'); 
  else if (is_quad) jsmr_context.Emit('4ofakind', '1'); 
  else if (is_trip && is_pair) jsmr_context.Emit('fullhouse', '1'); 
  else if (is_flush) jsmr_context.Emit('flush', '1'); 
  else if (is_straight) jsmr_context.Emit('straight', '1'); 
  else if (is_trip) jsmr_context.Emit('3ofakind', '1'); 
  else if (is_two_pair) jsmr_context.Emit('2pair', '1'); 
  else if (is_pair) jsmr_context.Emit('pair', '1'); 
  else jsmr_context.Emit('highcard', '1'); 
} 
