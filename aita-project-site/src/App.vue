<script setup lang="ts">
import Row from "./components/Row.vue";
import SingleRow from "./components/SingleRow.vue";
import TwoChart from "./components/TwoChart.vue";
</script>

<template>
  <v-menu class="menu">
    <template v-slot:activator="{ props }">
      <v-btn color="primary" v-bind="props"> More</v-btn>
    </template>
    <v-list>
      <a href="https://github.com/dbarkowsky/AITA-Analysis">
        <v-list-item>
          <v-list-item-title>GitHub</v-list-item-title>
        </v-list-item>
      </a>
      <a href="https://www.reddit.com/r/AmItheAsshole/">
        <v-list-item>
          <v-list-item-title>r/AmItheAsshole</v-list-item-title>
        </v-list-item>
      </a>
    </v-list>
  </v-menu>
  <v-container fluid class="main-container">
    <v-row justify="center" align-content="center">
      <v-col lg="7" md="9" sm="12">
        <h1>r/AmItheAsshole</h1>
        <h3>A Data Survey</h3>
      </v-col>
    </v-row>
    <SingleRow v-slot:childSlot>
      <p>
        If you're not familiar with it,
        <a href="https://www.reddit.com/r/AmItheAsshole/">r/AmItheAsshole</a>
        is a forum on the website
        <a href="https://www.reddit.com/">Reddit</a> that revolves around one
        thing: <b>judgement</b>.
      </p>
      <p>
        Users will post their stories looking for the assessment of their Reddit
        peers. The best of these stories are often tales of insane family
        members, bitter significant others, or petty acts of revenge.
      </p>
      <p>
        In the end, users will vote with the first line of their comments using
        acronyms like YTA or NTA. After 18 hours, the verdict is in as the
        top-rated comment has their vote applied to the post as a flair.
      </p>
      <p class="left-text">For example:</p>
      <img class="styled-image" src="/assets/images/sample_post.png" />
    </SingleRow>
    <Row
      title="The Original Hypothesis"
      img="/assets/charts/scatterplot_LikelihoodofAssholeifRomanticandOlderbyAgeDifference.svg"
      v-slot:childSlot
    >
      <p>Let's cut right to the chase.</p>
      <p>
        My wife browses a lot of r/AmItheAsshole. Over time she felt like she
        noticed a particular trend:
        <b
          >posts where the original poster (OP) was writing about their romantic
          partner and where the OP was the older of the two</b
        >
        were more likely to be branded as assholes.
      </p>
      <p>
        The bigger the gap between the OP and the person they were writing
        about, the greater the chance that they would be viewed as assholes.
      </p>
      <p>
        This was the crux of the whole project, and as you can see from this
        chart, it wasn't a bad hypothesis. As the age gap between OP and partner
        widens, the asshole-ery starts to trend up.
      </p>
    </Row>
    <SingleRow v-slot:childSlot>
      <p>
        This does tend to get a little bit hazier as the age gap widens, just
        because there are fewer data points to help calculate this gap. Early
        on, there's a 70/30 split in how these two flairs are assigned, but once
        that age gap hits the 20-year mark, it becomes practically even.
      </p>
      <p>
        The underlying factor for this trend isn't clear though, and if you're
        also a browser of this subreddit, you probably know there are more than
        two flairs though, so let's talk about...
      </p>
    </SingleRow>
    <Row
      title="Methodology"
      img="/assets/images/code_snippet.png"
      v-slot:childSlot
      dark="true"
    >
      <p>
        Starting on 2023-06-07, I started collecting posts from r/AmItheAsshole
        by running a Python script that simply reached out to Reddit's API
        endpoint and saved the information from each post into a .csv file for
        that day.
      </p>
      <p>
        If I had more forethought, I would have probably set this to repeat
        automatically, but instead I ran that script on a frequent basis until
        2023-10-17. There were absolutely posts missed in this time, but the
        bulk of them were represented. Reddit's API has some interesting
        restrictions regarding how far you can reach back in time. In all,
        35,078 posts were collected, which is way more than the 10,000 I
        originally aimed for.
      </p>
      <p>
        With a growing number of .csv files, I used additional Python scripts to
        combine the individual files into a single file that removed the raw
        information like the text of the post but added calculated information
        like the OP's gender and age and whether or not the post seemed to be
        about a romantic partner.
      </p>
    </Row>
    <SingleRow v-slot:childSlot dark="true">
      <p>
        A final Python script was created to take this calculated data and
        actually tally up totals, get means and medians, and finally create
        charts to visualize the outcome.
      </p>
      <p>Only four flairs were looked at for this project:</p>
      <v-row>
        <v-col sm="3" cols="6"><b>Not the A-hole</b></v-col>
        <v-col sm="3" cols="6"><b>Asshole</b></v-col>
        <v-col sm="3" cols="6"><b>No A-holes here</b></v-col>
        <v-col sm="3" cols="6"><b>Everyone Sucks</b></v-col>
      </v-row>
      <p>
        The other flairs were a lot more muddy in their assignment and meaning.
        Even the latter two I was on the fence about including, as they are only
        somewhat direct opposites on the flair scale like the first two are and
        they don't have nearly as many occurrences.
      </p>
    </SingleRow>
    <Row
      title="Charts You Came For"
      img="\assets\charts\bar_CountofPostbyFlair.svg"
      v-slot:childSlot
    >
      <p>
        There's a clear winner here when it comes to the most common flair.
        About three times as many OPs are considered not assholes in their
        respective situations.
      </p>
      <p>
        It's not as clear to tell which posts the community is actually
        enjoying. Non-aholes seem to get scored higher than the assholes. This
        means they are getting more upvotes (and maybe less downvotes).
        Hopefully they aren't downvoted based on opinion of the OP.
      </p>
      <p>
        There tend to be a lot more comments for asshole posts, which I imagine
        is because there are generally more arguments on those posts. The posts
        where Everyone Sucks are also hot topics of conversations. Maybe it's
        because those are often the craziest stories.
      </p>
    </Row>
    <SingleRow v-slot:childSlot>
      <p>
        Another explanation for the lower average number of comments for the Not
        the A-hole flair is that there are simply a lot more of them that don't
        get much engagement at all. Out of curiosity I checked the medians for
        this as well, and the results are fairly similar with the only really
        difference is that Everyone Sucks is a tiny bit lower.
      </p>
    </SingleRow>
    <TwoChart
      img1="\assets\charts\bar_AveragePostScoreperFlair.svg"
      img2="\assets\charts\bar_AverageNumberofCommentsperFlair.svg"
    ></TwoChart>
    <SingleRow v-slot:childSlot title="A Story of the Ages" dark="true">
      <p>
        A lot of the data that I collected was centred around ages. I was
        curious to know what ages most commonly posted to the subreddit and
        whether people's opinions of them might be influenced by that age.
      </p>
    </SingleRow>
    <Row
      img="\assets\charts\stacked_bar_CountofAgeofPosters.svg"
      dark="true"
      v-slot:childSlot
    >
      <p>
        I was glad to see a fairly normal distribution here. To me at least,
        this makes sense with the age that we would start seeing people active
        in the community and also the older ages that might make up less of
        Reddit's population (or maybe are less likely to air their dirty laundry
        there).
      </p>
      <p>
        From this view, there's not really an obvious trend relating age to
        asshole-ery.
      </p>
      <p>
        For the reader, age and gender were determined as best as possible based
        on words proceeding what I'm calling "identifiers." These often look
        like (M32), but can come in many forms.
      </p>
      <p>
        If there was a pronoun such as <b>I, me, or myself</b> before an
        identifier, I took that as a high chance the identifier belonged to the
        poster.
      </p>
    </Row>
    <Row
      dark="true"
      img="\assets\charts\scatterplot_LikelihoodofAssholebyAgeofPoster.svg"
      v-slot:childSlot
    >
      <p>
        I was pleasantly surprised to find that there's a decent correlation
        between age of the OP and the likelihood they are to be rated an
        asshole.
      </p>
      <p>
        We're only looking at two flairs here, so it's expected that they look
        pretty close the mirror images of each other, but the consistency of the
        lower ages and then seeing how that 35-40 range starts creating assholes
        is an interesting picture.
      </p>
      <p>
        Again, there are significantly less data points for posts with ages
        greater than 35, so we see the trend start to spread out. I'm hopeful
        that with additional data this spread might start to tighten up.
      </p>
    </Row>
    <SingleRow dark="true" v-slot:childSlot>
      <p>
        I also tried breaking down these ages into brackets. These results are
        telling a similar story as the information above.
      </p>
      <p>
        The main bulk of posters are still below 35 years of age, and as the age
        increases, more of those OPs are being considered assholes by the
        community. I find it a little funny that the Everybody Sucks flair gets
        so little love for the >45 bracket. At this point, maybe people just
        feel like "no, you are old enough and should have known better."
      </p>
    </SingleRow>
    <TwoChart
      dark="true"
      img2="\assets\charts\stacked_bar_RatioofPostsperAgeBracketperFlair.svg"
      img1="\assets\charts\bar_CountofPostsperAgeBracketperFlair.svg"
    />
    <SingleRow dark="true" v-slot:childSlot>
      <p>
        The final age-based experiment was focused around the difference in
        years between the OP and the other participant in the post. In order to
        make this work, only posts with two identifiers were included, so
        there's no way to tell if the OP is talking about multiple parties.
      </p>
      <p>
        This was my chance to use a pyramid chart. I was so preoccupied with
        whether or not I could, I didn't stop to think if I should. Jokes aside,
        I'm not sold on how it expresses this age difference, but it does do a
        decent job of showing that the bulk of posts don't have much of an age
        difference at all.
      </p>
      <p>
        This isn't too surprising. People are likely to complain about their
        significant others, and they tend to be close in age.
      </p>
      <p>
        You can see in the scatterplot that there's a reason why most charts cut
        out around the 50-60 mark. There just aren't many posts with gaps that
        large, so we end up with very polarized results. Even in the more
        consistent section, there doesn't appear to be a correlation between age
        gap and asshole-ery.
      </p>
    </SingleRow>
    <TwoChart
      dark="true"
      img2="\assets\charts\scatterplot_LikelihoodofAssholebyAgeGap.svg"
      img1="\assets\charts\pyramid_CountofAgeDifferenceperFlair.svg"
    />
    <Row
      v-slot:childSlot
      title="The Sex-y Part"
      img="\assets\charts\bar_GenderTrendsbyCount.svg"
    >
      <p>
        I looked at two different metrics for gender. Normally people will mark
        their identifiers with an M or an F, so it's tough to get more nuanced
        information about how the OP identifies other than that. I was also
        interested in whether there was a difference if all the identifiers were
        the same gender or not.
      </p>
      <p>
        That last part was looked at in two different ways, one with only two
        participants and one with any number. The only difference was fewer
        overall, but the spread was similar.
      </p>
      <p>
        It's notable that there are significantly more female posters here,
        which is almost opposite of the global Reddit gender distribution from
        2022 (<a
          href="https://www.statista.com/statistics/1255182/distribution-of-users-on-reddit-worldwide-gender/"
          >Statista</a
        >).
      </p>
      <p>
        Not surprisingly, it's more likely that not all participants will be the
        same gender, especially when the number of participants grows.
      </p>
    </Row>
    <Row
      v-slot:childSlot
      img="\assets\charts\stacked_bar_GenderTrendsbyRatioofPosts.svg"
    >
      <p>
        Moreover, the ratio of asshole to not-asshole is a bit worse for male
        OPs, about 22.5%. Female OPs on the other hand have about a 13.8%
        asshole rate.
      </p>
      <p>
        Perhaps this could be related to the previously mentioned balance of
        male and female users, assuming the people voting have the same gender
        distribution as the people posting.
      </p>
      <p>
        Whether the same or different gender between all participants, it
        doesn't seem to affect the asshole rate.
      </p>
    </Row>
    <SingleRow v-slot:childSlot title="The Extras" dark="true">
      <p>
        The final two categories that I was hoping would be more fruitful were
        seeing how often a post is edited and seeing how often a post might be
        considered romantic. <b>Romantic</b> for this purpose is anytime there's
        a mention of someone who might fit as a significant other. Words like
        <b>boyfriend, wife, etc.</b> will count.
      </p>
      <p>
        This is an extremely messy category, because it's very likely that
        people would mention those people but not have the post mainly about
        them. They could be mentioned as a one-off, and it would still count.
      </p>
      <p>
        The results here were a little disappointing. For edited posts, it's
        more common that they would be assholes on a per-post basis when
        compared to their non-edited counterparts. Could this be because people
        who are assholes are trying to defend themselves or is it more likely
        that they become the asshole after editing something particularly nasty
        in. It would be interesting to see when they edited the post, before or
        after flair assignment.
      </p>
      <p>
        Romantic status was a complete bust. The categories are so even, it's
        not super relevant either way.
      </p>
    </SingleRow>
    <TwoChart
      dark="true"
      img1="\assets\charts\bar_DistributionofFlairsbyEditedStatus.svg"
      img2="\assets\charts\bar_DistributionofFlairsbyRomanticStatus.svg"
    />
    <Row
      v-slot:childSlot
      img="\assets\charts\horizontal_bar_Top10MostFrequentPosters.svg"
      title="The Top Dogs"
    >
      <p>
        This category belongs to the people who are the most frequent posters.
        Maybe they actually have a lot of problems to share with the community,
        but maybe they're also just in it for the Reddit karma.
      </p>
      <p>
        u/crowbass222 currently has the lead, but others are close behind. He
        literally posted another one right as I updated these tables before
        posting! If there were a larger database of posts, it would be
        interesting to see who the top posters of all time were.
      </p>
    </Row>
    <SingleRow v-slot:childSlot dark="true" title="So Long, Farewell...">
      <p>
        I'm not a data scientist or a statistician, but I had a lot of fun doing
        this and learned a lot too. There are definitely some improvements to
        make here, but I hope you found this interesting.
      </p>
      <p>
        If you are interested at all in the code that makes this run, follow the
        <b>More</b> button at the top of the screen to visit the GitHub
        repository or take a peek at my portfolio site to see what else I'm up
        to.
      </p>
    </SingleRow>
  </v-container>
</template>

<style scoped lang="scss">
@import "./colours.scss";
.main-container {
  background-color: $beige;
  color: $text-dark;
  width: 100vw;
  padding: 2em 0 0 0;
}

.v-col {
  padding: 0.5em 2em;

  p {
    margin: 1em;
  }
}

.left-text {
  text-align: left;
}

.styled-image {
  border: 0.5em solid $red;
  border-radius: 1em;
  width: 100%;
}

.v-list {
  padding: 0;
}

.v-list,
.v-list-item,
.v-list-item-title {
  color: $text-dark;
  :hover {
    background-color: $orange;
    transition: 0.5s;
  }
}

@supports selector(:focus-visible) {
  .v-btn {
    position: fixed !important;
    top: 0.5em;
    left: 0.5em;
    background-color: $red !important;
    color: $text-dark !important;
  }
}
</style>
